#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from agenda.models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Clases que gestiona CRUD+L de Contactos

class ContactListView(ListView):
    context_object_name = 'contact_list' 

    def get_queryset(self):
        return Contact.objects.order_by('first_name')#[:5]

class ContactCreateView(CreateView):
    model = Contact
    success_url = '/agenda/'

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    
    def get_success_url(self):
        return reverse('agenda:detail', kwargs={'pk': self.object.pk,})
    
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/agenda/'