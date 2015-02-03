from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from agenda import views


urlpatterns = patterns('',
    # ex: /agenda/
    url(r'^$', login_required(views.ContactListView.as_view()), name='list'),
    # ex: /agenda/create/
    url(r'^create/$', login_required(views.ContactCreateView.as_view()), name='create'),
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name='detail'),
    # ex: /agenda/1/update/
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ContactUpdateView.as_view()), name='update'),
    # ex: /agenda/1/delete/
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.ContactDeleteView.as_view()), name='delete'),
    # ex: /agenda/search/?contactFilter
    #url(r'^search/$', views.ContactSearchView.as_view(), name='search'),
    url(r'^search/$', login_required(views.search), name='search'),
)