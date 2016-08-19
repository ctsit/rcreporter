"""
This module is to create ModelFrom for models inorder to provide
easy rendering of models at front-end.
"""

from django import forms
from .models import Queries, Proj_Exec_TimeStmp
from bootstrap_toolkit.widgets import BootstrapDateInput

class QueriesForm(forms.ModelForm):
	"""
	ModelFrom for the Queries model.

	This model is not currently in use. But can be included 
	in future work to introduce addition of new queries for tables 
	in database.
	"""

	query_text = forms.CharField(widget=forms.Textarea)
	query_sql = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Queries
		fields = ['query_text', 'query_sql']
		exclude = ['pub_date']
