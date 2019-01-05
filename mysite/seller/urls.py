from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^index/$", views.index, name="index"),
    url(r"^seller_login/$", views.seller_login, name="seller_login"),
    url(r"^seller_register/$", views.seller_register, name="seller_register"),
    url(r"^check_code/$", views.check_code, name="check_code"),
    url(r"^seller_logout/$", views.seller_logout, name="seller_logout"),
    url(r"^seller_Center/$", views.seller_Center, name="seller_Center"),
]