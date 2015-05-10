import datetime
import cStringIO
import sys
from urllib import unquote

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import InMemoryUploadedFile

import bikephototag.apps.phototag.models as models
import bikephototag.apps.phototag.forms as forms

import django_couch
db = django_couch.db()

class Login(TemplateView):
    template_name = 'phototag/login.html'
    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['login_form'] = forms.LoginForm()
        context['registration_form'] = forms.RegistationForm()
        return context

class Profile(TemplateView):
    template_name = 'phototag/profile.html'
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user_info'] = {
            'name': 'Steph',
            'score': '15',
            'last_challenge_won': 'String of some sort',
        } 
        return context


class Leaderboard(TemplateView):
    template_name = 'phototag/leaderboard.html'
    def get_context_data(self, **kwargs):
        context = super(Leaderboard, self).get_context_data(**kwargs)
        context['leaderboard'] = [
            {
                'user': {
                    'username': 'steph',
                    'get_absolute_url': '/p/21/',
                },
                'score': 15,
                'last_challenge_won': 'String of some sort',
            },
            {
                'user': {
                    'username': 'steph',
                    'get_absolute_url': '/p/21/',
                },
                'score': 15,
                'last_challenge_won': 'String of some sort',
            },
            {
                'user': {
                    'username': 'steph',
                    'get_absolute_url': '/p/21/',
                },
                'score': 15,
                'last_challenge_won': 'String of some sort',
            },
        ]
        return context


class Index(TemplateView):
    template_name = 'phototag/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['locations'] = []
        for location in models.Location.objects.all():
            context['locations'].append(location.menu_dict())
        return context


class LocationDetail(TemplateView):
    template_name = 'phototag/location_detail.html'

    def get_context_data(self, **kwargs):
        location_id = int(kwargs['location_id'])
        location = models.Location.objects.get(pk=location_id)
        context = super(LocationDetail, self).get_context_data(**kwargs)
        context['location'] = location.menu_dict()
        return context


class NewLocationEvent(FormView):
    template_name = 'phototag/location_event.html'
    form_class = forms.AddPhotoForm

    def get_context_data(self, **kwargs):
        context = super(NewLocationEvent, self).get_context_data(**kwargs)
        # FIXME: user id from the event
        # location_id = int(kwargs['location_id'])
        location_id = 1
        location = models.Location.objects.get(pk=location_id)
        context['location'] = location.menu_dict()
        return context

    def post(self, request, *args, **kwargs):
        file_field=request.POST['img']

        if file_field.startswith('data:'):
            params, data = file_field.split(',', 1)
            params = params[5:] or 'text/plain;charset=US-ASCII'
            params = params.split(';')
            if not '=' in params[0] and '/' in params[0]:
                mimetype = params.pop(0)
            else:
                mimetype = 'text/plain'
            if 'base64' in params:
                # handle base64 parameters first
                data = data.decode('base64')
            for param in params:
                if param.startswith('charset='):
                    # handle characterset parameter
                    data = unquote(data).decode(param.split('=', 1)[-1])

        file = cStringIO.StringIO(data)
        image = InMemoryUploadedFile(file,
           field_name='file',
           name='capture.png',
           content_type=mimetype,
           size=sys.getsizeof(file),
           charset=None)

        request.FILES[u'file'] = image

        # FIXME: user id from the event
        location_id = 1
        location = models.Location.objects.get(pk=location_id)

        doc_id = db.create({'type': 'foundphoto', 'djangoid': location_id})
        db.put_attachment({'_id': doc_id, '_rev': db.get(doc_id)['_rev']},
                content=image, filename='capture.png')

        current_event = models.PhotoEvent.objects.all().order_by('-date_added')[0]
        current_event.found_photo_couch_id = doc_id
        current_event.found_photo=request.FILES['file']
        current_event.finding_user = request.user
        current_event.date_found = datetime.datetime.now()
        current_event.save()

        return HttpResponseRedirect('/%s/next/' % location.id)

class AddNewLocation(FormView):
    form_class = forms.AddPhotoForm

    def post(self, request, *args, **kwargs):
        file_field=request.POST['img']

        if file_field.startswith('data:'):
            params, data = file_field.split(',', 1)
            params = params[5:] or 'text/plain;charset=US-ASCII'
            params = params.split(';')
            if not '=' in params[0] and '/' in params[0]:
                mimetype = params.pop(0)
            else:
                mimetype = 'text/plain'
            if 'base64' in params:
                # handle base64 parameters first
                data = data.decode('base64')
            for param in params:
                if param.startswith('charset='):
                    # handle characterset parameter
                    data = unquote(data).decode(param.split('=', 1)[-1])

        file = cStringIO.StringIO(data)
        image = InMemoryUploadedFile(file,
           field_name='file',
           name='capture.png',
           content_type=mimetype,
           size=sys.getsizeof(file),
           charset=None)
        request.FILES[u'file'] = image

        # FIXME: user id from the event
        location_id = 1
        location = models.Location.objects.get(pk=location_id)

        doc_id = db.create({'type': 'photo', 'djangoid': location_id})
        db.put_attachment({'_id': doc_id, '_rev': db.get(doc_id)['_rev']},
                content=image, filename='capture.png')

        next_event = models.PhotoEvent(latitude=1, longitude=1)
        next_event.user = request.user
        next_event.photo_couch_id = doc_id
        next_event.photo=request.FILES['file']
        next_event.save()

        return HttpResponseRedirect('/%s/' % location.id)
