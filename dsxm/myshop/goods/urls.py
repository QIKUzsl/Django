from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "store"
urlpatterns = [
    url(r"^(?P<g_id>\d+)/detail/$", views.detail, name="detail"),
    url(r"^add/$", views.add, name="add"),
    url(r"^findTypeByPid/$", views.findTypeByPid, name="findTypeByPid"),

]