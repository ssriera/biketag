from django.shortcuts import render
import bikephototag.apps.phototag.models as models
import bikephototag.apps.phototag.forms as forms
from django.views.generic import TemplateView, FormView
import datetime
import cStringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from urllib import unquote

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
           #size=len(file.getvalue()),
           charset=None)
        request.FILES[u'file'] = image

        location_id = 1
        location = models.Location.objects.get(pk=location_id)
        current_event = models.PhotoEvent.objects.all().order_by('-date_found')[0]
        current_event.photo=request.FILES['file']
        current_event.finding_user = request.user
        current_event.date_found = datetime.datetime.now()
        current_event.save()
