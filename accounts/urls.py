from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.sign_in, name='login'),
    url(r'^logout/$', views.sing_out, name='logout'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
]
