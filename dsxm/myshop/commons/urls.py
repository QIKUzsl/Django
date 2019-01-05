from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r"^(?P<s_id>\d+)/index/$", views.index, name="index"),

    url(r"^$", views.index, name="index"),

]