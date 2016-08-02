from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Queries
from .forms import QueriesForm
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the dashboard for sql queries")

def queries_create(request):
	if request.method=='POST':
		form = QueriesForm(request.POST)
		print "Lets see what happens"
		if form.is_valid():
			form.pub_date = datetime.now().strftime("%m/%d/%Y")
			form.save()
			return HttpResponseRedirect('success')
		else:
			print "It is not valid"
			return render(request, 'reportingTool/error.html', {'form':form.errors})
	else:
		form = QueriesForm()
		return render(request, 'reportingTool/queries.html', {'form':form})

def queries(request):
	details = Queries.objects.all()
	context = {
	'title':'Queries',
	'objects':details,
	}
	return render(request, 'reportingTool/details.html', context)
