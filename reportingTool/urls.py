"""
Contains the url for reaching out to pages for the reportingTool app.
"""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'project/', views.ProjectFilterSingleTableView.as_view(), name='project'),
    url(r'site/', views.SiteFilterSingleTableView.as_view(), name='site'),
    url(r'projExec/', views.ProjExecFilterSingleTableView.as_view(), name='projExec'),
    url(r'siteReport/', views.SiteReportFilterSingleTableView.as_view(), name='siteReport')
    
    ## Url links for Queries table (Future Work)
    # url(r'queryCreate', views.query_create, name='Query Create'),
    # url(r'queryUpdate/(?P<id>\d+)', views.query_update, name="Query Update"),
    # url(r'queryDetails', views.QueryFilterSingleTableView.as_view()),
]
