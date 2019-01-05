from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
   url(r"^admin/", admin.site.urls),
   url(r"^index/$", views.index, name="index"),
   url(r"^login/$", views.login, name="login"),
   url(r"^update_login/$", views.update_login, name="update_login"),
   url(r"^register/$", views.register, name="register"),
   url(r"^add_register/$", views.add_register, name="add_register"),
   url(r"^register_ajax/$", views.register_ajax, name="register_ajax"),
   url(r"^check_code/$", views.check_code, name="check_code"),
   url(r"^logout/$", views.logout, name="logout"),
   url(r"^sends/$", views.sends, name="sends"),
]