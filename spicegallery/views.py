from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.db.models import Count

from .models import SpiceGallery, SpiceMix

total_spices_per_mix = SpiceMix.objects.values('name').annotate(Count('spices'))

def enough_spices_selected_for_mix(total_spices, selected_spices):
    if total_spices < 4:
        return selected_spices >= total_spices
    elif total_spices == 4:
        return selected_spices >= total_spices - 1
    elif total_spices < 8:
        return selected_spices >= total_spices - 2
    else:
        return selected_spices >= total_spices - 3


class IndexView(generic.ListView):
    template_name = 'spicegallery/index.html'
    context_object_name = 'spice_list'

    def get_queryset(self):
        return SpiceGallery.objects.order_by('name')

    def post(self, request):
        return HttpResponseRedirect(reverse('spicegallery:mixes'))


class MixView(generic.ListView):
    template_name = 'spicegallery/mixes.html'

    def get_queryset(self, request):
        return request.POST.getlist('spice')

    def post(self, request):
        mixes_with_enough_spices = []
        selected_spices = request.POST.getlist('spice')
        mixes = SpiceMix.objects.filter(spices__name__in=selected_spices).values('name').annotate(Count('name'))
        for mix in mixes:
            mix_name = mix['name']
            spices_selected_for_mix = mix['name__count']
            total_spices = total_spices_per_mix.get(name=mix_name)['spices__count']
            if enough_spices_selected_for_mix(total_spices, spices_selected_for_mix):
                mixes_with_enough_spices += [mix_name]
        mixes_list = SpiceMix.objects.filter(name__in=mixes_with_enough_spices)
        if not selected_spices:
            return HttpResponseRedirect(reverse('spicegallery:index'))
        return render(request, self.template_name, {'mixes_list' : mixes_list, 'spice_list': selected_spices})
