from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^addArcticle_ajax/$', views.addArcticle_ajax,name="addArcticle_ajax"),
    url(r'^register1/$', views.register1,name="register1"),
    url(r'^rep/$', views.rep,name="rep"),
    url(r'^list_article/$', views.list_article,name="list_article"),
    url(r'^text/$', views.text,name="text"),
    url(r'^delUser/$', views.delUser,name="delUser"),
    url(r'^updateUser/$', views.updateUser,name="updateUser"),
    url(r'^createCode/$', views.createCode,name="createCode"),
    url(r'^addArcticle/$', views.addArcticle,name="addArcticle"),
    url(r'^list_users/$', views.list_users,name="list_users"),
    url(r'^text1/$', views.text1,name="text1"),
    url(r'^register/$', views.register,name="register"),
    url(r'^login/$', views.login,name="login"),
    url(r'^home/$', views.home,name="home"),
]
