from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Queries
from .forms import QueriesForm
from datetime import datetime

# Create your views here.
def index(request):
    items = Queries.objects.all()
    objects = []
    fields = items[0]._meta
    for item in items:
        query_Text = str(fields.get_field('query_text').value_to_string(item))
        query_Sql = str(fields.get_field('query_sql').value_to_string(item))
        objects.append((query_Text, query_Sql))
    
    context = {
    'title': 'Dashboard',
    'objects': objects,
    }
    return render(request, 'reportingTool/main.html', context)

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
    items = Queries.objects.all()
    objects = []
    for item in items:
        objects.append([str(field.value_to_string(item)) for field in item._meta.fields])
    context = {
    'title':'Queries',
    'objects':objects,
    }
    return render(request, 'reportingTool/details.html', context)
