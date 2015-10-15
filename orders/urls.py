from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<order_id>[0-9]+)/execute/$', views.IndexView.as_view(), name='execute'),
]
