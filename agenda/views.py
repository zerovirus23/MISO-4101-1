#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from agenda.models import Contact, Localization
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'agenda/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.order_by('first_name')#[:5]

class DetailView(generic.DetailView):
    model = Contact
    template_name = 'agenda/detail.html'
