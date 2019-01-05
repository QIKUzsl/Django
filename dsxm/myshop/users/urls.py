from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^user_login/$", views.user_login, name="user_login"),
    url(r"^register/$", views.register, name="register"),
    url(r"^user_logout/$", views.user_logout, name="user_logout"),
    url(r"^check_code/$", views.check_code, name="check_code"),
    url(r"^userInfo/$", views.userInfo, name="userInfo"),
    url(r"^createCode/$", views.createCode, name="createCode"),
    url(r"^updateUser/$", views.updateUser, name="updateUser"),
    url(r"^add_address/$", views.add_address, name="add_address"),
    url(r"^address_list/$", views.address_list, name="address_list"),
    # url(r"^reg_email/$", views.reg_email, name="reg_email"),
    # url(r"^active/(?P<token>.*)/$", views.active, name="active"),
]