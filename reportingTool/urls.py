from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'queryDetails', views.list_queries, name='Query Details'),
    url(r'queryCreate', views.query_create, name='Query Create'),
    url(r'queryUpdate/(?P<id>\d+)', views.query_update, name="Query Update"),
    url(r'people', views.people, name='People'),
    url(r'charts', views.charts, name='Charts'),
    url(r'(?P<poll_id>\d+)/canvas.png$', views.canvas),
    url(r'test/', views.test, name='test'),
    url(r'filter', views.QueryFilterSingleTableView.as_view()),
    url(r'project', views.project, name='project'),
    url(r'site/', views.site, name='site'),
    url(r'projExec', views.projExec, name='projExec'),
    url(r'siteReport', views.siteReport, name='siteReport')

]
