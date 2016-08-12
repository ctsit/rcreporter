import django_filters
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports ,Queries
from bootstrap_toolkit.widgets import BootstrapDateInput

class ProjectsFilter(django_filters.FilterSet):
	class Meta:
		model = Projects

class SitesFilter(django_filters.FilterSet):
	siteName = django_filters.CharFilter(name='siteName', lookup_expr='icontains')
	class Meta:
		model = Sites

class ProjExecFilter(django_filters.FilterSet):
	startTimeStmp = django_filters.DateTimeFromToRangeFilter(name='startTimeStmp')
	endTimeStmp = django_filters.DateTimeFromToRangeFilter(name='endTimeStmp')
	class Meta:
		model = Proj_Exec_TimeStmp

class SiteReportsFilter(django_filters.FilterSet):
	class Meta:
		model = Site_Reports

class QueryFilter(django_filters.FilterSet):
	query_sql = django_filters.CharFilter(name='query_sql', lookup_expr='icontains')
	query_text = django_filters.CharFilter(name='query_text', lookup_expr='icontains')
	pub_date = django_filters.DateRangeFilter(name='pub_date')
	class Meta:
		model = Queries
		