from django.conf.urls import url
from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from AP_Agenda.settings import *

app_name = 'agenda'

urlpatterns = [
    # Examples:
    # url(r'^$', 'AP_Agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    re_path(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    #url(r'^$', RedirectView.as_view(url='/index.')),
    re_path(r'^agenda/', include('agenda.urls')),
    path('admin/', admin.site.urls),
    #re_path(r'^admin/', admin.site.urls),
    #re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/$', views.LoginView.as_view(template_name='registration/login.html')),
    re_path(r'^logout/$',views.LogoutView.as_view(),{'next_page': '/'}), 
]
