from django.shortcuts import render#, get_object_or_404
#from django.http import HttpResponse
from django.urls import reverse
#from django.core.urlresolvers import reverse
from agenda.models import Agenda, Contact, Grupo, ContactNetwork, Localization
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import redirect
from agenda.DB import  mytimer
from agenda.correo import  correo
#from agenda.DB.mytimer import tempo


#==========================================================
#Clases que gestiona CRUD+L de Agenda
#==========================================================
class AgendaListView(ListView):
    model = Agenda
    context_object_name = 'agenda_list' 
    
    def get_queryset(self):
        #t = mytimer.tempo()
        #t.iniciar()
        c = correo.myCorreo()
        print("hello world")
        c.enviarGmail()
        print ("hello world2")
        user = self.request.user;
        print ("hello world3")
        return Agenda.objects.all().filter(user_id = user.id)

class AgendaListPublicView(ListView):
    context_object_name = 'agenda_list' 
    
    def get_queryset(self):
        return Agenda.objects.all().filter(type = 1) #El 1 es para agendas públicas
    

class AgendaCreateView(CreateView):
    model = Agenda
    fields = ['name', 'type', 'grupo']
    success_url = '/agenda/'

    def form_valid(self, form):
        user = self.request.user
        #form.instance.grupo.queryset = Grupo.objects.filter(users__id = user.id)
        form.instance.user = self.request.user
        return super(AgendaCreateView, self).form_valid(form)
class AgendaDetailView(DetailView):
    model = Agenda
    
class AgendaUpdateView(UpdateView):
    model = Agenda
    
    def get_success_url(self):
        return reverse('agenda:agenda_detail', kwargs={'pk': self.object.pk,})
    
class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = '/agenda/'
#==========================================================
#Clases que gestiona CRUD+L de Grupo
#==========================================================
class GrupoListView(ListView):
    context_object_name = 'grupo_list' 
    
    def get_queryset(self):
        user = self.request.user
        return Grupo.objects.filter(users__id = user.id)

class AgendaGrupoListView(ListView):
    context_object_name = 'agenda_list' 
    template_name = 'agenda/grupo_agenda_list.html'
    def get(self, request, *args, **kwargs):
        if ('grupo_id' in self.request.GET) or ('grupo_id' in self.request.session):
            return super(AgendaGrupoListView, self).get(self, request, *args, **kwargs);
        else:
            return redirect('/agenda/grupo')
    def get_queryset(self):
        if 'grupo_id' in self.request.GET:
            grupo_param_id = self.request.GET['grupo_id']
            self.request.session['grupo_id'] = grupo_param_id
        elif 'grupo_id' in self.request.session:
            grupo_param_id = self.request.session['grupo_id']
        
        return Agenda.objects.filter(grupo__id = grupo_param_id)
    
        
class GrupoCreateView(CreateView):
    model = Grupo
    fields = ['name', 'users']
    success_url = '/agenda/grupo/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GrupoCreateView, self).form_valid(form)

class GrupoDetailView(DetailView):
    model = Grupo
    
class GrupoUpdateView(UpdateView):
    model = Grupo
    
    def get_success_url(self):
        return reverse('agenda:grupo_detail', kwargs={'pk': self.object.pk,})
    
    
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
        #t = mytimer.tempo()
        #t.detener()
        if 'agenda_id' in self.request.GET:
            agenda_param_id = self.request.GET['agenda_id']
            self.request.session['agenda_id'] = agenda_param_id
        elif 'agenda_id' in self.request.session:
            agenda_param_id = self.request.session['agenda_id']
        
        return Contact.objects.all().filter(agenda_id = agenda_param_id)
        
class ContactCreateView(CreateView):
    #t = mytimer.tempo()
    #t.detener()
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
    
    def get_success_url(self):
        return reverse('agenda:localization_detail', kwargs={'pk': self.object.pk,})
    
class LocalizationDeleteView(DeleteView):
    model = Localization
    success_url = '/agenda/contact/localization'



#==========================================================
#Clases que gestiona CRUD+L de Localizaciones
#==========================================================
class ColoresListView(ListView):
    
    context_object_name = 'colores_list' 
    
    def get_queryset(self):
        t = mytimer.tempo()
        t.iniciar()
        user = self.request.user;
        return Colores.objects.all().filter(user_id = user.id)


    def get(self, request, *args, **kwargs):
        if ('contact_id' in self.request.GET) or ('contact_id' in self.request.session):
            return super(ColoresListView, self).get(self, request, *args, **kwargs);
        else:
            return redirect('/agenda/color')
        
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
    
    def get_success_url(self):
        return reverse('agenda:localization_detail', kwargs={'pk': self.object.pk,})
    
class LocalizationDeleteView(DeleteView):
    model = Localization
    success_url = '/agenda/contact/localization'
    
