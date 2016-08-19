"""
This module contains the views for the reportingTool app.

The view class is responsible for taking the web requests and returns a web response.
The response is returned by rendering HTML content based on respective template.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QueriesForm
from datetime import datetime
from django_tables2 import RequestConfig, SingleTableView
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports, Queries
from .filters import ProjectsFilter, SitesFilter, ProjExecFilter, SiteReportsFilter, QueryFilter
from .tables import ProjectsTable, SitesTable, ProjExecTable, SiteReportsTable,QueriesTable

# Create your views here.

class FilteredSingleTableView(SingleTableView):
    """
    A class based view.

    This view is acting as a base class for all the models in the database. 
    All the models are inheriting this base class to render themselves with 
    the functionality of 'filtering', 'table', and 'charts'.
    The main page/ dashboard is getting rendered using this view.
    """

    filter_class = None
    template_name = 'reportingTool/listTables.html'
    table_pagination = {
        'per_page': 20
    }
    col = None
    pivot = False

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_chart(self):
        if self.pivot:
            # This section of code use Pivot Charts.

            if self.col is None:
                return None 
            xData = self.col[0]
            yData  = self.col[1]
            
            ds = PivotDataPool(
                series=
                [{'options': {
                    'source': self.filter.qs,
                    'categories': xData},
                    'terms' : {
                    'tot_exec': ([yData])
                    }
                }])
            cht = PivotChart(
                datasource = ds,
                series_options =
                [{ 'options': {
                    'type': 'column',
                    'stacking': False},
                    'terms': ['tot_exec']
                    }],
                chart_options =
                {'title': {
                    'text': 'CHARTS'},
                'xAxis': {
                    'title' : {
                    'text': 'Project Name'
                    }}})
            return cht
        else:
            # This section of code use Charts.
            if self.col is None:
                return None 
            xData = self.col[0]
            yData  = self.col[1]
            print xData, yData
            ds = DataPool(
                series=
                [{'options': {
                    'source': self.filter.qs },
                    'terms' : [
                    xData,
                    yData ]}
                ])
            cht = Chart(
                datasource = ds,
                series_options =
                [{ 'options': {
                    'type': 'column',
                    'stacking': False},
                    'terms':{
                        xData: [
                        yData ]
                    }}],
                chart_options =
                {'title': {
                    'text': 'CHARTS'},
                'xAxis': {
                    'title' : {
                    'text': 'Project Name'
                    }}})
            return cht

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        context['chart'] = self.get_chart()
        return context

class ProjectFilterSingleTableView(FilteredSingleTableView):
    """This class based view is used for Projects model.
    
    The col variable is used to provide the field values for charts.
    The first column represents the field on the X axis 
    and second column represents the field on the Y axis.
    """
    
    model = Projects
    table_class = ProjectsTable
    filter_class = ProjectsFilter
    #col = ['projectName', 'projectID']    

   
class SiteFilterSingleTableView(FilteredSingleTableView):
    """This class based view is used for Sites model. """

    model = Sites
    table_class = SitesTable
    filter_class = SitesFilter

class ProjExecFilterSingleTableView(FilteredSingleTableView):
    """This class based view is used for Proj_Exec_TimeStmp model.
    
    The col variable is used to provide the field values for charts.
    The first column represents the field on the X axis 
    and second column represents the field on the Y axis.
    """

    model = Proj_Exec_TimeStmp
    table_class = ProjExecTable
    filter_class = ProjExecFilter
    #col = ['startTimeStmp', 'project__projectName']

class SiteReportFilterSingleTableView(FilteredSingleTableView):
    """This class based view is used for Site_Reports model.
    
    The col variable is used to provide the field values for charts.
    The first column represents the field on the X axis 
    and second column represents the field on the Y axis.
    """

    model = Site_Reports
    table_class = SiteReportsTable
    filter_class = SiteReportsFilter
    col = ['site__siteName', 'patientCount']

def index(request):
    """
    # Possibly this feature can be added in future
    items = Queries.objects.all()
    queryObjects = getItemsList(items, True)

    """
    context = {
    'title': 'Dashboard',
    #'queryObjects': queryObjects,
    }
    return render(request, 'reportingTool/main.html', context)

"""This class is presently not been used.
But as a part of future work we can have a Query class,
which will be used add new queries related to tables in database.


class QueryFilterSingleTableView(FilteredSingleTableView):
    model = Queries
    table_class = QueriesTable
    filter_class = QueryFilter


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

"""




