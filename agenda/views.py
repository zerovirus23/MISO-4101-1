from django.shortcuts import render#, get_object_or_404
#from django.http import HttpResponse
from django.core.urlresolvers import reverse
from agenda.models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

def search(request):
    if 'contactFilter' in request.GET:
        filter_param = request.GET['contactFilter']
        
        if(filter_param):
            contacts = Contact.objects.filter(Q(first_name__contains=filter_param)|Q(last_name__contains=filter_param))#[:5]
        else:
            contacts = Contact.objects.all()
            
    return render(request, 'agenda/contact_list.html', {'contact_list': contacts,'contactFilter': filter_param})