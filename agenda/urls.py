from django.conf.urls import patterns, url

from agenda import views


urlpatterns = patterns('',
    # ex: /agenda/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)