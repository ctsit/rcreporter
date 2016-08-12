from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QueriesForm, dates
from datetime import datetime
from django_tables2 import RequestConfig, SingleTableView
from .models import Projects, Sites, Proj_Exec_TimeStmp, Site_Reports, Queries
from .filters import ProjectsFilter, SitesFilter, ProjExecFilter, SiteReportsFilter, QueryFilter
from .tables import ProjectsTable, SitesTable, ProjExecTable, SiteReportsTable,QueriesTable

class FilteredSingleTableView(SingleTableView):
    filter_class = None
    template_name = 'reportingTool/list.html'
    table_pagination = {
        'per_page': 25
    }

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context

class ProjectFilterSingleTableView(FilteredSingleTableView):
    model = Projects
    table_class = ProjectsTable
    filter_class = ProjectsFilter

class SiteFilterSingleTableView(FilteredSingleTableView):
    model = Sites
    table_class = SitesTable
    filter_class = SitesFilter

class ProjExecFilterSingleTableView(FilteredSingleTableView):
    model = Proj_Exec_TimeStmp
    table_class = ProjExecTable
    filter_class = ProjExecFilter

class SiteReportFilterSingleTableView(FilteredSingleTableView):
    model = Site_Reports
    table_class = SiteReportsTable
    filter_class = SiteReportsFilter

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
    #query.paginate(page=request.GET.get('page', 1), per_page=5)
    RequestConfig(request, paginate={'per_page':25}).configure(query)
    return render(request, 'reportingTool/people.html', {'query':query, 'request':request})


def charts(request):
    import random
    import django
    import datetime
    
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def canvas(request, poll_id):
    import matplotlib
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    fig = Figure()

    ax=fig.add_subplot(1,1,1)
    ps = Site_Reports.objects.filter(exec_ID__timeStmpID=poll_id) # Get the poll object from django

    x = matplotlib.numpy.arange(1,len(ps))
    
    votes = [choice.patientCount for choice in ps]
    names = [choice.site_ID for choice in ps]


    numTests = len(ps)
    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups

    ax.bar(ind, votes)


    ax.set_xticks(ind+0.5)
    ax.set_xticklabels(names)


    ax.set_xlabel("Site IDs")
    ax.set_ylabel("Patient Count")

    #ax.set_xticklabels(names)

    title = u"Dynamically Generated Results Plot for Sites"#: %s" % p.question"
    ax.set_title(title)


    #ax.grid(True)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')

    canvas.print_png(response)
    return response

def test(request):
    form = dates()
    return render(request, 'reportingTool/test.html', {'form':form})
