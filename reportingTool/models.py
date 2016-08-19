"""
This module contais the module description for this Django Project.
"""

from __future__ import unicode_literals
from django.db import models
from datetime import date



# Create your models here.

class Projects(models.Model):
    """
    Model for Projects table.
    """

    projectID = models.AutoField(primary_key=True, verbose_name='Project ID')
    projectName = models.CharField(max_length=1000, verbose_name='Project Name')

    class Meta:
        db_table = "PROJECTS"

    def __unicode__(self):
        return self.projectName

class Sites(models.Model):
    """
    Model for Sites table.
    """

    siteID = models.AutoField(primary_key=True, verbose_name='Site ID')
    siteName = models.CharField(max_length=1000, verbose_name='Site Name')
    project = models.ForeignKey(Projects, verbose_name='Project')

    class Meta:
        db_table = "SITES"

    def __unicode__(self):
        return self.siteName

class Proj_Exec_TimeStmp(models.Model):
    """
    Model for Proj_Exec_TimeStmp table.
    """

    timeStmpID = models.AutoField(primary_key=True, verbose_name='TimeStamp ID')
    startTimeStmp = models.DateField(verbose_name='Start TimeStamp')
    endTimeStmp = models.DateField(verbose_name='End TimeStamp')
    project = models.ForeignKey(Projects, verbose_name='Project')

    class Meta:
        db_table = "PROJ_EXEC_TIMESTMP"

    def __unicode__(self):
        return str(self.startTimeStmp.strftime("%m/%d/%Y")) + ' - ' + str(self.endTimeStmp.strftime("%m/%d/%Y"))

class Site_Reports(models.Model):
    """
    Model for Site_Reports table.
    """

    reportID = models.AutoField(primary_key=True, verbose_name='Report ID')
    patientCount = models.IntegerField(verbose_name='Patient Count')
    projExec = models.ForeignKey(Proj_Exec_TimeStmp, db_column='exec_ID', verbose_name='TimeStamp ID')
    site = models.ForeignKey(Sites, verbose_name='Site Name')

    class Meta:
        db_table = "SITE_REPORTS"

    def __unicode__(self):
        return str(self.reportID)

class Queries(models.Model):
    """
    Model for Queries table.
    """

    query_text = models.CharField(verbose_name='Query Text', max_length=1000)
    query_sql = models.CharField(verbose_name='Query SQL', max_length=1000)
    pub_date = models.DateField(verbose_name='Published Date', default=date.today)

    class Meta:
        db_table = "QUERIES"

    def __unicode__(self):
        return self.query_text




