from __future__ import unicode_literals

from django.db import models
from datetime import date



# Create your models here.

class Projects(models.Model):
	projectID = models.AutoField(primary_key=True, verbose_name='Project ID')
	projectName = models.CharField(max_length=1000, verbose_name='Project Name')

	class Meta:
		db_table = "PROJECTS"

	def __unicode__(self):
		return self.projectName

class Sites(models.Model):
	siteID = models.AutoField(primary_key=True, verbose_name='Site ID')
	siteName = models.CharField(max_length=1000, verbose_name='Site Name')
	project_ID = models.ForeignKey(Projects, db_column='project_ID', verbose_name='Project')

	class Meta:
		db_table = "SITES"

	def __unicode__(self):
		return self.siteName

class Proj_Exec_TimeStmp(models.Model):
	timeStmpID = models.AutoField(primary_key=True, verbose_name='TimeStamp ID')
	startTimeStmp = models.DateTimeField(verbose_name='Start TimeStamp')
	endTimeStmp = models.DateTimeField(verbose_name='End TimeStamp')
	project_ID = models.ForeignKey(Projects, db_column='project_ID', verbose_name='Project')

	class Meta:
		db_table = "PROJ_EXEC_TIMESTMP"

	def __unicode__(self):
		return str(self.startTimeStmp.strftime("%m/%d/%Y %I:%M %a")) + ' - ' + str(self.endTimeStmp.strftime("%Y-%m-%d %I:%M %p"))

class Site_Reports(models.Model):
	reportID = models.AutoField(primary_key=True, verbose_name='Report ID')
	patientCount = models.IntegerField(verbose_name='Patient Count')
	exec_ID = models.ForeignKey(Proj_Exec_TimeStmp, db_column='exec_ID', verbose_name='TimeStamp ID')
	site_ID = models.ForeignKey(Sites, db_column='site_ID', verbose_name='Site Name')

	class Meta:
		db_table = "SITE_REPORTS"

	def __unicode__(self):
		return str(self.reportID)

class Queries(models.Model):
    query_text = models.CharField(verbose_name='Query Text', max_length=1000)
    query_sql = models.CharField(verbose_name='Query SQL', max_length=1000)
    pub_date = models.DateField(verbose_name='Published Date', default=date.today)

    class Meta:
    	db_table = "QUERIES"

    def __unicode__(self):
    	return self.query_text




