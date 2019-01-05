from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/', views.login,name='login'),
    url(r'^register/', views.register,name='register'),
    url(r'^createCode/', views.createCode,name='createCode'),
    url(r'^home/', views.home,name='home'),
    url(r'^base/', views.base,name='base'),
    url(r'^user_info/', views.user_info,name='user_info'),
    url(r'^add_Article/', views.add_Article,name='add_Article'),
]
