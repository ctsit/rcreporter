from django import forms
from .models import Queries

class QueriesForm(forms.ModelForm):
	query_text = forms.CharField(widget=forms.Textarea)
	query_sql = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Queries
		fields = ['query_text', 'query_sql']
		exclude = ['pub_date']
