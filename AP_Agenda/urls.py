from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AP_Agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^$', RedirectView.as_view(url='/admin/')),
    url(r'^agenda/', include('agenda.urls', namespace='agenda')),
    url(r'^admin/', include(admin.site.urls)),
)
