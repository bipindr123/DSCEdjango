from django.shortcuts import render
from .models import FundedProject, Proposal
from django.db.models import *

all_projects = FundedProject.objects.all()
all_proposals = Proposal.objects.all()
all_years = FundedProject.objects.order_by('-start_date__year').values('start_date__year').distinct()
all_years2 = Proposal.objects.order_by('-submission_date__year').values('submission_date__year').distinct()
# Create your views here.

def index(request):
    pass

def projects(request):
    global all_projects
    all_projects = FundedProject.objects.all()
    total = all_projects.count()
    total_amount = all_projects.aggregate(Sum('amount_sactioned'))
    context = {
        'all_projects': all_projects,
        'all_years': all_years,
        'total': total,
        'total_amount': total_amount,
    }
    return render(request, 'projects/index.html', context)


def search_projects(request):
    global all_projects
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)

        if (search_year == ''):
            all_projects = FundedProject.objects.filter(
                title__contains=search_query).__or__(FundedProject.objects.filter(pi_designation__contains=search_query)).filter(
                dept__contains=search_dept)
        else:
            all_projects = FundedProject.objects.filter(
                title__contains=search_query).__or__(FundedProject.objects.filter(pi_designation__contains=search_query)).filter(
                dept__contains=search_dept,start_date__year=search_year)
        # Do whatever you need with the word the user looked for
        # Your code
        total = all_projects.count()
        total_amount = all_projects.aggregate(Sum('amount_sactioned'))
        context = {
            'all_projects': all_projects,
            'all_years': all_years,
            'total': total,
            'total_amount': total_amount
        }
    return render(request, 'projects/index.html', context)

def proposals(request):
    global all_proposals
    all_proposals = Proposal.objects.all()
    total = all_proposals.count()
    total_amount = all_proposals.aggregate(Sum('p_amount_applied'))
    context = {
        'all_proposals': all_proposals,
        'all_years': all_years2,
        'total': total,
        'total_amount': total_amount
    }
    return render(request, 'projects/index2.html', context)


def search_proposals(request):
    global all_proposals
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        search_dept = request.GET.get('search_param1', None)
        search_year = request.GET.get('search_param2', None)

        if (search_year == ''):
            all_proposals = Proposal.objects.filter(
                title__contains=search_query).__or__(Proposal.objects.filter(pi_designation__contains=search_query)).filter(
                dept__contains=search_dept)
        else:
            all_proposals = Proposal.objects.filter(
                title__contains=search_query).__or__(Proposal.objects.filter(pi_designation__contains=search_query)).filter(
                dept__contains=search_dept,submission_date__year=search_year)
        # Do whatever you need with the word the user looked for
        # Your code
        total = all_proposals.count()
        total_amount = all_proposals.aggregate(Sum('p_amount_applied'))
        context = {
            'all_proposals': all_proposals,
            'all_years': all_years2,
            'total': total,
            'total_amount': total_amount
        }
    return render(request, 'projects/index2.html', context)



