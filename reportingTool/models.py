from __future__ import unicode_literals

from django.db import models
from django.utils import timezone



# Create your models here.

class Queries(models.Model):
    query_text = models.CharField(max_length=1000)
    query_sql = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __unicode__(self):
    	return self.query_text


