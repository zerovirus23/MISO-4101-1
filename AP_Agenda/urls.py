from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AP_Agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^agenda/', include('agenda.urls', namespace='agenda')),
    url(r'^admin/', include(admin.site.urls)),
)
