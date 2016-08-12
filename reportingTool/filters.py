import django_filters
from .models import Queries

class QueryFilter(django_filters.FilterSet):
	query_sql = django_filters.CharFilter(name='query_sql', lookup_expr='icontains')
	class Meta:
		model = Queries