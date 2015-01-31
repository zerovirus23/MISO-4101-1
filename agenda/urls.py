from django.conf.urls import patterns, url

from agenda import views


urlpatterns = patterns('',
    # ex: /agenda/
    url(r'^$', views.ContactListView.as_view(), name='list'),
    # ex: /agenda/create/
    url(r'^create/$', views.ContactCreateView.as_view(), name='create'),
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='detail'),
    # ex: /agenda/1/update/
    url(r'^(?P<pk>\d+)/update/$', views.ContactUpdateView.as_view(), name='update'),
    # ex: /agenda/1/delete/
    url(r'^(?P<pk>\d+)/delete/$', views.ContactDeleteView.as_view(), name='delete'),
    # ex: /agenda/search/?contactFilter
    #url(r'^search/$', views.ContactSearchView.as_view(), name='search'),
    url(r'^search/$', views.search, name='search'),
)