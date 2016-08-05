from __future__ import unicode_literals

from django.db import models
from datetime import date



# Create your models here.

class Projects(models.Model):
	projectID = models.AutoField(primary_key=True)
	projectName = models.CharField(max_length=1000)

	class Meta:
		db_table = "PROJECTS"

	def __unicode__(self):
		return self.projectName

class Sites(models.Model):
	siteID = models.AutoField(primary_key=True)
	siteName = models.CharField(max_length=1000)
	project_ID = models.ForeignKey(Projects, db_column='project_ID')

	class Meta:
		db_table = "SITES"

	def __unicode__(self):
		return self.siteName

class Proj_Exec_TimeStmp(models.Model):
	timeStmpID = models.AutoField(primary_key=True)
	startTimeStmp = models.DateTimeField()
	endTimeStmp = models.DateTimeField()
	project_ID = models.ForeignKey(Projects, db_column='project_ID')

	class Meta:
		db_table = "PROJ_EXEC_TIMESTMP"

	def __unicode__(self):
		return self.timeStmpID

class Site_Reports(models.Model):
	reportID = models.AutoField(primary_key=True)
	patientCount = models.IntegerField()
	exec_ID = models.ForeignKey(Proj_Exec_TimeStmp, db_column='exec_ID')
	site_ID = models.ForeignKey(Sites, db_column='site_ID')

	class Meta:
		db_table = "SITE_REPORTS"

	def __unicode__(self):
		return self.reportID

class Queries(models.Model):
    query_text = models.CharField(max_length=1000)
    query_sql = models.CharField(max_length=1000)
    pub_date = models.DateField('date published', default=date.today)

    class Meta:
    	db_table = "QUERIES"

    def __unicode__(self):
    	return self.query_text




