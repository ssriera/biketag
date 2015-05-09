from django.shortcuts import render
import .models

class Index(TemplateView):
    template_name = '/phototag/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['locations'] = models.Location.objects.all()

# class LocationList(TemplateView):
#     template_name = '/phototag/index.html'
#     def get_context_data(self, **kwargs):
#         context = super(GroupSetDetail, self).get_context_data(**kwargs)
