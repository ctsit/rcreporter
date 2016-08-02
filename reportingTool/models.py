from __future__ import unicode_literals

from django.db import models
from datetime import date



# Create your models here.

class Queries(models.Model):
    query_text = models.CharField(max_length=1000)
    query_sql = models.CharField(max_length=1000)
    pub_date = models.DateField('date published', default=date.today)

    def __unicode__(self):
    	return self.query_text


