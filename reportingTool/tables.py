import django_tables2 as tables
from .models import Projects, Sites, Site_Reports, Proj_Exec_TimeStmp, Queries

class ProjectsTable(tables.Table):
	class Meta:
		model = Projects

class SitesTable(tables.Table):
	class Meta:
		model = Sites

class ProjExecTable(tables.Table):
	class Meta:
		model = Proj_Exec_TimeStmp

class SiteReportsTable(tables.Table):
	class Meta:
		model = Site_Reports

class QueriesTable(tables.Table):
	class Meta:
		model = Queries
		# add class="paleblue" to <table> tag
		
