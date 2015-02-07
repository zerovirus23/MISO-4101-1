from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AP_Agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    #url(r'^$', RedirectView.as_view(url='/index.')),
    url(r'^agenda/', include('agenda.urls', namespace='agenda')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^static/$', include('agenda.static')),
)
