from django.conf.urls import url
from django.urls import include, path, re_path
from django.contrib.auth.decorators import login_required
from agenda import views
from AP_Agenda import settings


urlpatterns = [
    # ex: /agenda/
    re_path(r'^$', login_required(views.AgendaListView.as_view()), name='agenda_list'),
    
    #re_path(r'^agenda/grupo/$', login_required(views.AgendaGrupoListView.as_view()), name='agenda_grupo_list'),
    # ex: /agenda/public
    re_path(r'^public/$', login_required(views.AgendaListPublicView.as_view()), name='agenda_list'),
    # ex: /agenda/create/
    re_path(r'^create/$', login_required(views.AgendaCreateView.as_view()), name='agenda_create'),
    # ex: /agenda/5/
    re_path(r'^(?P<pk>\d+)/$', login_required(views.AgendaDetailView.as_view()), name='agenda_detail'),
    # ex: /agenda/1/update/
    re_path(r'^(?P<pk>\d+)/update/$', login_required(views.AgendaUpdateView.as_view()), name='agenda_update'),
    # ex: /agenda/1/delete/
    re_path(r'^(?P<pk>\d+)/delete/$', login_required(views.AgendaDeleteView.as_view()), name='agenda_delete'),                 
    
    
    # ex: /grupo/
    re_path(r'^grupo/$', login_required(views.GrupoListView.as_view()), name='grupo_list'),
   
    # ex: /grupo/create/
    re_path(r'^grupo/create/$', login_required(views.GrupoCreateView.as_view()), name='grupo_create'),
    
    re_path(r'^grupo/(?P<pk>\d+)/agendas/$', login_required(views.AgendaGrupoListView.as_view()), name='grupo_agenda_list'),
    
    # ex: /grupo/5/
    re_path(r'^grupo/(?P<pk>\d+)/$', login_required(views.GrupoDetailView.as_view()), name='grupo_detail'),
    # ex: /grupo/1/update/
    re_path(r'^grupo/(?P<pk>\d+)/update/$', login_required(views.GrupoUpdateView.as_view()), name='grupo_update'),
    
    #re_path(r'^grupo/(?P<pk>\d+)/agendas/$', login_required(views.GrupoAgendasView.as_view()), name='grupo_agendas_list'),
    # ex: /grupo/1/delete/
    #re_path(r'^grupo/(?P<pk>\d+)/delete/$', login_required(views.GrupoDeleteView.as_view()), name='grupo_delete'), 
           
    # ex: /agenda/contact
    re_path(r'^contact/$', login_required(views.ContactListView.as_view()), name='contact_list'),
    # ex: /agenda/create/
    re_path(r'^contact/create/$', login_required(views.ContactCreateView.as_view()), name='contact_create'),
    # ex: /agenda/5/
    re_path(r'^contact/(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name='contact_detail'),
    # ex: /agenda/1/update/
    re_path(r'^contact/(?P<pk>\d+)/update/$', login_required(views.ContactUpdateView.as_view()), name='contact_update'),
    # ex: /agenda/1/delete/
    re_path(r'^contact/(?P<pk>\d+)/delete/$', login_required(views.ContactDeleteView.as_view()), name='contact_delete'),
    # ex: /agenda/contact/search/?contactFilter
    re_path(r'^contact/search/$', login_required(views.contact_search), name='contact_search'),
    
    
    # ex: /agenda/contact/network
    re_path(r'^contact/network/$', login_required(views.NetworkListView.as_view()), name='network_list'),
    # ex: /agenda/create/
    re_path(r'^contact/network/create/$', login_required(views.NetworkCreateView.as_view()), name='network_create'),
    # ex: /agenda/5/
    re_path(r'^contact/network/(?P<pk>\d+)/$', login_required(views.NetworkDetailView.as_view()), name='network_detail'),
    # ex: /agenda/1/update/
    re_path(r'^contact/network/(?P<pk>\d+)/update/$', login_required(views.NetworkUpdateView.as_view()), name='network_update'),
    # ex: /agenda/1/delete/
    re_path(r'^contact/network/(?P<pk>\d+)/delete/$', login_required(views.NetworkDeleteView.as_view()), name='network_delete'),
    
     # ex: /agenda/contact/localization
    re_path(r'^contact/localization/$', login_required(views.LocalizationListView.as_view()), name='localization_list'),
    # ex: /agenda/create/
    re_path(r'^contact/localization/create/$', login_required(views.LocalizationCreateView.as_view()), name='localization_create'),
    # ex: /agenda/5/
    re_path(r'^contact/localization/(?P<pk>\d+)/$', login_required(views.LocalizationDetailView.as_view()), name='localization_detail'),
    # ex: /agenda/1/update/
    re_path(r'^contact/localization/(?P<pk>\d+)/update/$', login_required(views.LocalizationUpdateView.as_view()), name='localization_update'),
    # ex: /agenda/1/delete/
    re_path(r'^contact/localization/(?P<pk>\d+)/delete/$', login_required(views.LocalizationDeleteView.as_view()), name='localization_delete'),
    
]

#urlpatterns += patterns('',
#    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#)