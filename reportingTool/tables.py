"""
Module to implement table functionality for all the models.

This module uses django_tables2 to implement the tables.
The use of default django_tables2 enables to generate table including all
the fields as column for the give model.
"""

import django_tables2 as tables
from .models import Projects, Sites, Site_Reports, Proj_Exec_TimeStmp, Queries

class ProjectsTable(tables.Table):
	"""Implement table over Projects model. """
	class Meta:
		model = Projects

class SitesTable(tables.Table):
	"""Implement table over Sites model. """
	class Meta:
		model = Sites

class ProjExecTable(tables.Table):
	"""Implement table over Proj_Exec_TimeStmp model. """
	class Meta:
		model = Proj_Exec_TimeStmp

class SiteReportsTable(tables.Table):
	"""Implement table over Site_Reports model. """
	projectName = tables.Column(accessor='site.project')
	class Meta:
		model = Site_Reports

class QueriesTable(tables.Table):
	"""Implement table over Queries model. """
	class Meta:
		model = Queries