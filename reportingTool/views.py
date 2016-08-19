from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QueriesForm, dates
from datetime import datetime
from django_tables2 import RequestConfig, SingleTableView
from chartit import DataPool, Chart
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports, Queries
from .filters import ProjectsFilter, SitesFilter, ProjExecFilter, SiteReportsFilter, QueryFilter
from .tables import ProjectsTable, SitesTable, ProjExecTable, SiteReportsTable,QueriesTable

class FilteredSingleTableView(SingleTableView):
    filter_class = None
    template_name = 'reportingTool/list.html'
    table_pagination = {
        'per_page': 25
    }
    col = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_chart(self):
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
                'type': 'line',
                'stacking': False},
                'terms':{
                    xData: [
                    yData ]
                }}],
            chart_options =
            {'title': {
                'text': 'HEy wahts up!!!'},
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
    model = Projects
    table_class = ProjectsTable
    filter_class = ProjectsFilter
    col = ['projectName', 'projectID']    

   
class SiteFilterSingleTableView(FilteredSingleTableView):
    model = Sites
    table_class = SitesTable
    filter_class = SitesFilter

class ProjExecFilterSingleTableView(FilteredSingleTableView):
    model = Proj_Exec_TimeStmp
    table_class = ProjExecTable
    filter_class = ProjExecFilter
    col = ['startTimeStmp', 'project_ID__projectName']

class SiteReportFilterSingleTableView(FilteredSingleTableView):
    model = Site_Reports
    table_class = SiteReportsTable
    filter_class = SiteReportsFilter
    col = ['site_ID__siteName', 'patientCount']

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

# Create your views here.
def index(request):
    items = Queries.objects.all()
    queryObjects = getItemsList(items, True)

    # projects = ProjectsTable(Projects.objects.all())
    # #projects.paginate(page=request.GET.get('page', 1), per_page=25)
    # RequestConfig(request, paginate={'per_page':25}).configure(projects)

    # sites = SitesTable(Sites.objects.all())
    # #sites.paginate(page=request.GET.get('page', 1), per_page=25)
    # RequestConfig(request, paginate={'per_page':25}).configure(sites)

    # projExecs = ProjExecTable(Proj_Exec_TimeStmp.objects.all())
    # #projExecs.paginate(page=request.GET.get('page', 1), per_page=25)
    # RequestConfig(request, paginate={'per_page':25}).configure(projExecs)

    # siteReports = SiteReportsTable(Site_Reports.objects.all())
    # #siteReports.paginate(page=request.GET.get('page', 1), per_page=25)
    # RequestConfig(request, paginate={'per_page':25}).configure(siteReports)

    context = {
    'title': 'Dashboard',
    'queryObjects': queryObjects,
    # 'projects': projects,
    # 'sites': sites,
    # 'projExecs': projExecs,
    # 'siteReports': siteReports 
    }
    return render(request, 'reportingTool/main.html', context)

def project(request):
    projects = ProjectsTable(Projects.objects.all())
    RequestConfig(request, paginate={'per_page':25}).configure(projects)
    return render(request, 'reportingTool/project.html', {'projects':projects})

def site(request):
    sites = SitesTable(Sites.objects.all())
    RequestConfig(request, paginate={'per_page':25}).configure(sites)
    return render(request, 'reportingTool/site.html', {'sites':sites})

def projExec(request):
    projExecs = ProjExecTable(Proj_Exec_TimeStmp.objects.all())
    RequestConfig(request, paginate={'per_page':25}).configure(projExecs)
    return render(request, 'reportingTool/projExec.html', {'projExec':projExecs})

def siteReport(request):
    siteReports = SiteReportsTable(Site_Reports.objects.all())
    RequestConfig(request, paginate={'per_page':25}).configure(siteReports)
    return render(request, 'reportingTool/siteReport.html', {'siteReport':siteReports})

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
    RequestConfig(request, paginate={'per_page':25}).configure(query)
    return render(request, 'reportingTool/people.html', {'query':query, 'request':request})
