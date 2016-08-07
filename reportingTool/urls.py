from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'queryDetails', views.list_queries, name='Query Details'),
    url(r'queryCreate', views.query_create, name='Query Create'),
    url(r'queryUpdate/(?P<id>\d+)', views.query_update, name="Query Update"),
    url('people', views.people, name='People')
]
