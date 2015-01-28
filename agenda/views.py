#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from agenda.models import Contact
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

#Clases que gestiona CRUD+L de Contactos

class ContactListView(ListView):
    context_object_name = 'contact_list' 
    
    def get_queryset(self):
        return Contact.objects.all()
        
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
    
class ContactSearchView(View):
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        print("Acá por lo menos ya llegó!")
        print("::: ")
        print(self.kwargs.get('contactFilter', 'CONTACT_FILTER IS EMPTY1'))
        filter_param = self.kwargs.get('contactFilter', '')
        
        if(filter_param):
            print("=====> Filter PARAM1 = " + filter_param)
            return Contact.objects.filter(Q(first_name__contains=filter_param)|Q(last_name__contains=filter_param))#[:5]
        else:
            print("=====> Filter PARAM2 = " + filter_param)
            return Contact.objects.all().order_by('first_name')#[:5]

    