from django import forms
from .models import Queries
from bootstrap_toolkit.widgets import BootstrapDateInput

class QueriesForm(forms.ModelForm):
	query_text = forms.CharField(widget=forms.Textarea)
	query_sql = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Queries
		fields = ['query_text', 'query_sql']
		exclude = ['pub_date']

class dates(forms.Form):
	date = forms.DateField(widget=BootstrapDateInput)