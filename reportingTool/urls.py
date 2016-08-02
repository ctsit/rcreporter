from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'queryDetails$', views.queries, name='Query Details'),
    url(r'queriesCreate', views.queries_create, name='Query Create')
]
