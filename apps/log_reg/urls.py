from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^main$', views.main),
    # url(r'^delete$', views.delete),
]
