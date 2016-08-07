import django_tables2 as tables
from .models import Queries

class QueriesTable(tables.Table):
	class Meta:
		model = Queries
		# add class="paleblue" to <table> tag
		attrs = {'class': 'paleblue'}
