from django.shortcuts import render, get_object_or_404
from .models import PhdStatus

# Create your views here.

all_statuses = PhdStatus.objects.all()
all_years = PhdStatus.objects.order_by('-year__year').values('year__year').distinct()


def index(request):
    global all_statuses
    all_statuses = PhdStatus.objects.all()
    total = all_statuses.count()
    context = {
        'all_statuses': all_statuses,
        'all_years': all_years,
        'total': total,
    }
    return render(request, 'Phdstatus/index.html', context)

def bob(request):
    global all_statuses
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)

        if (search_year == ''):
            all_statuses = PhdStatus.objects.filter(
                name__contains=search_query,dept__contains=search_dept)
        else:
            all_statuses = PhdStatus.objects.filter(
                name__contains=search_query, dept__contains=search_dept, year__year=search_year)
    total = all_statuses.count()
    context = {
        'all_statuses': all_statuses,
        'all_years': all_years,
        'total': total,
    }
    return render(request, 'Phdstatus/index.html', context)

def post(request, post_id):
    f_status = get_object_or_404(PhdStatus, pk=post_id)
    context = {
        'f_status':f_status,
    }
    return render(request, 'Phdstatus/print.html', context)
