from django.shortcuts import render#, get_object_or_404
#from django.http import HttpResponse
from django.core.urlresolvers import reverse
from agenda.models import Agenda, Contact, ContactNetwork, Localization
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import redirect


#==========================================================
#Clases que gestiona CRUD+L de Agenda
#==========================================================
class AgendaListView(ListView):
    context_object_name = 'agenda_list' 
    
    def get_queryset(self):
        user = self.request.user;
        return Agenda.objects.all().filter(user_id = user.id)
        
class AgendaCreateView(CreateView):
    model = Agenda
    fields = ['name']
    success_url = '/agenda/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AgendaCreateView, self).form_valid(form)

class AgendaDetailView(DetailView):
    model = Agenda
    
class AgendaUpdateView(UpdateView):
    model = Agenda
    fields = ['name']
    
    def get_success_url(self):
        return reverse('agenda:agenda_detail', kwargs={'pk': self.object.pk,})
    
class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = '/agenda/'
    
#==========================================================
#Clases que gestiona CRUD+L de Contactos
#==========================================================
class ContactListView(ListView):
    context_object_name = 'contact_list' 
    
    def get(self, request, *args, **kwargs):
        if ('agenda_id' in self.request.GET) or ('agenda_id' in self.request.session):
            return super(ContactListView, self).get(self, request, *args, **kwargs);
        else:
            return redirect('/agenda')
        
    def get_queryset(self):
        if 'agenda_id' in self.request.GET:
            agenda_param_id = self.request.GET['agenda_id']
            self.request.session['agenda_id'] = agenda_param_id
        elif 'agenda_id' in self.request.session:
            agenda_param_id = self.request.session['agenda_id']
        
        return Contact.objects.all().filter(agenda_id = agenda_param_id)
        
class ContactCreateView(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'company_name']
    success_url = '/agenda/contact'

    def form_valid(self, form):
        agenda_id = self.request.session['agenda_id']
        form.instance.agenda = Agenda.objects.get(pk=agenda_id)
        return super(ContactCreateView, self).form_valid(form)

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'company_name']
    
    def get_success_url(self):
        return reverse('agenda:contact_detail', kwargs={'pk': self.object.pk,})
    
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/agenda/contact'

def contact_search(request):
    if 'contactFilter' in request.GET:
        filter_param = request.GET['contactFilter']
        
        if(filter_param):
            contacts = Contact.objects.filter(Q(first_name__contains=filter_param)|Q(last_name__contains=filter_param))#[:5]
            return render(request, 'agenda/contact_list.html', {'contact_list': contacts,'contactFilter': filter_param})
    
    return redirect('/agenda/contact')


#==========================================================
#Clases que gestiona CRUD+L de Redes Sociales
#==========================================================
class NetworkListView(ListView):
    context_object_name = 'network_list' 
    
    def get(self, request, *args, **kwargs):
        if ('contact_id' in self.request.GET) or ('contact_id' in self.request.session):
            return super(NetworkListView, self).get(self, request, *args, **kwargs);
        else:
            return redirect('/agenda/contact')
        
    def get_queryset(self):
        if 'contact_id' in self.request.GET:
            contact_param_id = self.request.GET['contact_id']
            self.request.session['contact_id'] = contact_param_id
        elif 'contact_id' in self.request.session:
            contact_param_id = self.request.session['contact_id']
        
        return ContactNetwork.objects.all().filter(contact_id = contact_param_id)
        
class NetworkCreateView(CreateView):
    model = ContactNetwork
    fields = ['username', 'name']
    success_url = '/agenda/contact/network'
    
    def form_valid(self, form):
        contact_id = self.request.session['contact_id']
        form.instance.contact = Contact.objects.get(pk=contact_id)
        return super(NetworkCreateView, self).form_valid(form)

class NetworkDetailView(DetailView):
    context_object_name = 'network'
    model = ContactNetwork

class NetworkUpdateView(UpdateView):
    model = ContactNetwork
    fields = ['username', 'name']
    
    def get_success_url(self):
        return reverse('agenda:network_detail', kwargs={'pk': self.object.pk,})
    
class NetworkDeleteView(DeleteView):
    model = ContactNetwork
    success_url = '/agenda/contact/network'

#==========================================================
#Clases que gestiona CRUD+L de Localizaciones
#==========================================================
class LocalizationListView(ListView):
    context_object_name = 'localization_list' 
    
    def get(self, request, *args, **kwargs):
        if ('contact_id' in self.request.GET) or ('contact_id' in self.request.session):
            return super(LocalizationListView, self).get(self, request, *args, **kwargs);
        else:
            return redirect('/agenda/contact')
        
    def get_queryset(self):
        if 'contact_id' in self.request.GET:
            contact_param_id = self.request.GET['contact_id']
            self.request.session['contact_id'] = contact_param_id
        elif 'contact_id' in self.request.session:
            contact_param_id = self.request.session['contact_id']
        
        return Localization.objects.all().filter(contact_id = contact_param_id)
        
class LocalizationCreateView(CreateView):
    model = Localization
    fields = ['name','phone1','phone2','address1','address2','email1','email2']
    success_url = '/agenda/contact/localization'
    
    def form_valid(self, form):
        contact_id = self.request.session['contact_id']
        form.instance.contact = Contact.objects.get(pk=contact_id)
        return super(LocalizationCreateView, self).form_valid(form)

class LocalizationDetailView(DetailView):
    context_object_name = 'localization'
    model = Localization

class LocalizationUpdateView(UpdateView):
    model = Localization
    fields = ['name','phone1','phone2','address1','address2','email1','email2']
    
    def get_success_url(self):
        return reverse('agenda:localization_detail', kwargs={'pk': self.object.pk,})
    
class LocalizationDeleteView(DeleteView):
    model = Localization
    success_url = '/agenda/contact/localization'