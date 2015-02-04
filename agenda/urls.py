from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from agenda import views


urlpatterns = patterns('',
    # ex: /agenda/
    url(r'^$', login_required(views.AgendaListView.as_view()), name='agenda_list'),
    # ex: /agenda/create/
    url(r'^create/$', login_required(views.AgendaCreateView.as_view()), name='agenda_create'),
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', login_required(views.AgendaDetailView.as_view()), name='agenda_detail'),
    # ex: /agenda/1/update/
    url(r'^(?P<pk>\d+)/update/$', login_required(views.AgendaUpdateView.as_view()), name='agenda_update'),
    # ex: /agenda/1/delete/
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.AgendaDeleteView.as_view()), name='agenda_delete'),                 
                       
    # ex: /agenda/contact
    url(r'^contact/$', login_required(views.ContactListView.as_view()), name='contact_list'),
    # ex: /agenda/create/
    url(r'^contact/create/$', login_required(views.ContactCreateView.as_view()), name='contact_create'),
    # ex: /agenda/5/
    url(r'^contact/(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name='contact_detail'),
    # ex: /agenda/1/update/
    url(r'^contact/(?P<pk>\d+)/update/$', login_required(views.ContactUpdateView.as_view()), name='contact_update'),
    # ex: /agenda/1/delete/
    url(r'^contact/(?P<pk>\d+)/delete/$', login_required(views.ContactDeleteView.as_view()), name='contact_delete'),
    # ex: /agenda/contact/search/?contactFilter
    url(r'^contact/search/$', login_required(views.contact_search), name='contact_search'),
    
    
    # ex: /agenda/contact/network
    url(r'^contact/network/$', login_required(views.NetworkListView.as_view()), name='network_list'),
    # ex: /agenda/create/
    url(r'^contact/network/create/$', login_required(views.NetworkCreateView.as_view()), name='network_create'),
    # ex: /agenda/5/
    url(r'^contact/network/(?P<pk>\d+)/$', login_required(views.NetworkDetailView.as_view()), name='network_detail'),
    # ex: /agenda/1/update/
    url(r'^contact/network/(?P<pk>\d+)/update/$', login_required(views.NetworkUpdateView.as_view()), name='network_update'),
    # ex: /agenda/1/delete/
    url(r'^contact/network/(?P<pk>\d+)/delete/$', login_required(views.NetworkDeleteView.as_view()), name='network_delete'),
    
     # ex: /agenda/contact/localization
    url(r'^contact/localization/$', login_required(views.LocalizationListView.as_view()), name='localization_list'),
    # ex: /agenda/create/
    url(r'^contact/localization/create/$', login_required(views.LocalizationCreateView.as_view()), name='localization_create'),
    # ex: /agenda/5/
    url(r'^contact/localization/(?P<pk>\d+)/$', login_required(views.LocalizationDetailView.as_view()), name='localization_detail'),
    # ex: /agenda/1/update/
    url(r'^contact/localization/(?P<pk>\d+)/update/$', login_required(views.LocalizationUpdateView.as_view()), name='localization_update'),
    # ex: /agenda/1/delete/
    url(r'^contact/localization/(?P<pk>\d+)/delete/$', login_required(views.LocalizationDeleteView.as_view()), name='localization_delete'),
    
)