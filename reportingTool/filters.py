"""
Module to implement filter functionality for all the tables(models)

This module uses django_filters to implement the filters.
The use of default django_filters enables filters for all the fields present 
for the give model.
"""

import django_filters
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports ,Queries
from bootstrap_toolkit.widgets import BootstrapDateInput

class ProjectsFilter(django_filters.FilterSet):
	"""
	Implement filter over Projects model.

	The projectName field can be filtered on case insensitive data.
	It uses 'icontains' lookup, which means it would should all values which contains the
	data as shown in filter. 
	"""

	projectName = django_filters.CharFilter(name='projectName', lookup_expr='icontains')
	class Meta:
		model = Projects

class SitesFilter(django_filters.FilterSet):
	"""
	Implement filter over Sites model.

	The siteName field can be filtered on case insensitive data.
	It uses 'icontains' lookup, which means it would should all values which contains the
	data as shown in filter. 
	"""

	siteName = django_filters.CharFilter(name='siteName', lookup_expr='icontains')
	class Meta:
		model = Sites

class ProjExecFilter(django_filters.FilterSet):
	"""
	Implement filter over Proj_Exec_TimeStmp model.

	The startTimeStmp and endTimeStmp field can be filtered on DateTimeFromToRange filter.
	The DateTimeFromToRange filter will help in filtering data within a given range.
	"""

	startTimeStmp = django_filters.DateTimeFromToRangeFilter(name='startTimeStmp')
	endTimeStmp = django_filters.DateTimeFromToRangeFilter(name='endTimeStmp')
	class Meta:
		model = Proj_Exec_TimeStmp

class SiteReportsFilter(django_filters.FilterSet):
	"""
	Implement filter over Site_Reports model.
	"""

	class Meta:
		model = Site_Reports

class QueryFilter(django_filters.FilterSet):
	"""
	Implement filter over Queries model.

	This model is not being currently used, but can be considered in future work. 
	"""
	query_sql = django_filters.CharFilter(name='query_sql', lookup_expr='icontains')
	query_text = django_filters.CharFilter(name='query_text', lookup_expr='icontains')
	pub_date = django_filters.DateRangeFilter(name='pub_date')
	class Meta:
		model = Queries
		