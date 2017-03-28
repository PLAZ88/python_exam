from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index),
    url(r'^create', views.create),
    url(r'^(?P<id>\d+)', views.feature),
    url(r'^process', views.process),
    url(r'^delete/(?P<id>\d+)', views.delete),
    url(r'^remove/(?P<id>\d+)', views.remove),
    url(r'^repeatprocess/(?P<id>\d+)', views.repeatprocess),
    url(r'^delete', views.delete)

]

