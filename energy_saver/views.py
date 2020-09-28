from django.shortcuts import render
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'energy_saver/index.html'

    def get_queryset(self):
        print('hello')
        return 0

