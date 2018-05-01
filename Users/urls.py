from django.conf.urls import url
from Users import views

urlpatterns = [
    url(r'^users/$', views.getAllUser),
    url(r'^users/(?P<pk>[0-9]+)/$', views.getUserDetail),
]