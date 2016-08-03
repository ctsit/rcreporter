from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Queries
from .forms import QueriesForm
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the dashboard for sql queries")

def query_create(request):
	form = QueriesForm(request.POST or None)
	if request.method=='POST':
		print "Lets see what happens"
		if form.is_valid():
			print "Form is valid"
			form.pub_date = datetime.now().strftime("%m/%d/%Y")
			form.save()
			return HttpResponseRedirect('queryDetails')
		else:
			print "It is not valid"
			return render(request, 'reportingTool/error.html', {'form':form.errors})
	return render(request, 'reportingTool/queries.html', {'form':form})

def query_update(request, id):
	instance = get_object_or_404(Queries, pk=id)
	form = QueriesForm(request.POST or None, instance=instance)
	if request.method=='POST':
		if form.is_valid():
			form.pub_date = datetime.now().strftime("%m/%d/%Y")
			form.save()
			return HttpResponseRedirect('queryDetails')
		else:
			return render(request, 'reportingTool/error.html', {'form':form.errors})
	return render(request, 'reportingTool/queries.html', {'form':form})

def list_queries(request):
	details = Queries.objects.all()
	context = {
	'title':'Queries',
	'objects':details,
	}
	return render(request, 'reportingTool/details.html', context)
