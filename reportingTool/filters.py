import django_filters
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports ,Queries

class ProjectsFilter(django_filters.FilterSet):
	class Meta:
		model = Projects

class SitesFilter(django_filters.FilterSet):
	class Meta:
		model = Sites

class ProjExecFilter(django_filters.FilterSet):
	class Meta:
		model = Proj_Exec_TimeStmp

class SiteReportsFilter(django_filters.FilterSet):
	class Meta:
		model = Site_Reports

class QueryFilter(django_filters.FilterSet):
	query_sql = django_filters.CharFilter(name='query_sql', lookup_expr='icontains')
	class Meta:
		model = Queries