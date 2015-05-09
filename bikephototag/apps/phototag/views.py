from django.shortcuts import render
import bikephototag.apps.phototag.models as models
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'phototag/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['locations'] = []
        for location in models.Location.objects.all():
            context['locations'].append(location.menu_dict())
        return context

# class LocationList(TemplateView):
#     template_name = '/phototag/index.html'
#     def get_context_data(self, **kwargs):
#         context = super(GroupSetDetail, self).get_context_data(**kwargs)
