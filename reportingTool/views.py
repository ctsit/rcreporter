from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports, Queries
from .forms import QueriesForm
from datetime import datetime
from django_tables2 import RequestConfig
from .tables import QueriesTable

def getItemsList(items, dropDown=False):
    objects = []
    if dropDown:
        if len(items)>0:
            fields = items[0]._meta
            for item in items:
                query_Text = str(fields.get_field('query_text').value_to_string(item))
                query_Sql = str(fields.get_field('query_sql').value_to_string(item))
                objects.append((query_Text, query_Sql))
    else:
        for item in items:
            objects.append([str(field.value_to_string(item)) for field in item._meta.fields])
    return objects

# Create your views here.
def index(request):
    items = Queries.objects.all()
    queryObjects = getItemsList(items, True)

    items = Projects.objects.all()
    projectObjects = getItemsList(items)

    items = Sites.objects.all()
    siteObjects = getItemsList(items)
    print siteObjects

    items = Proj_Exec_TimeStmp.objects.all()
    execTmObjects = getItemsList(items)

    items = Site_Reports.objects.all()
    siteReportObjects = getItemsList(items)
    
    context = {
    'title': 'Dashboard',
    'queryObjects': queryObjects,
    'projectObjects': projectObjects,
    'siteObjects': siteObjects,
    'execTmObjects': execTmObjects,
    'siteReportObjects': siteReportObjects 
    }
    return render(request, 'reportingTool/main.html', context)

def query_create(request):
    form = QueriesForm(request.POST or None)
    if request.method=='POST':
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
    items = Queries.objects.all()
    objects = getItemsList(items)
    context = {
    'title':'Queries',
    'objects':objects,
    }
    return render(request, 'reportingTool/details.html', context)

def people(request):
    query = QueriesTable(Queries.objects.all())
    RequestConfig(request).configure(query)
    return render(request, 'reportingTool/people.html', {'query':query})