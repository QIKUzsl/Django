from django.conf.urls import url
from . import views
urlpatterns = [
   url('^home/$', views.home, name='home'),
   url('^update/$', views.update, name='update'),
   # url('^login_get/$', views.login_get, name='login_get'),
   # url('^text1/$', views.text1, name='text1'),
   # url('^register_success/$', views.register_success, name='register_success'),
   # url('^login_success/$', views.login_success, name='login_success'),
   # url('^register/$', views.register, name='register'),
   # url('^index/$', views.index, name='index'),
   # url('^index1/$', views.index1, name='index1'),
   url('^login/$', views.login, name='login'),
   url('^findall/$', views.findall, name='findall'),
   url('^findgood/$', views.findgood, name='findgood'),
   url('^findbad/$', views.findbad, name='findbad'),
   # url('^create_user/$', views.create_user, name='create_user'),
   url('^delete/$', views.delete, name='delete'),
   # url('^update/$', views.update, name='update'),
   url('^(\w+)/param', views.param, name='param'),
   url('^(?P<username>\w+)/param1', views.param1, name='param1'),
]