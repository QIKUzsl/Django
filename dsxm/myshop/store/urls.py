from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "store"
assert isinstance(settings, object)
urlpatterns = [
                  url(r"^add/$", views.add, name="add"),
                  url(r"^list/$", views.list, name="list"),
                  url(r"^store_base/$", views.store_base, name="store_base"),
                  url(r"^update/$", views.update, name="update"),
                  url(r"^(?P<s_id>\d+)/detail/$", views.detail, name="detail"),
                  url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/$", views.change, name="change"),

              ]