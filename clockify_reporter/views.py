from django.shortcuts import render
from .controllers.reporter import get_summary_report, get_tasks_report


def home(request):
    return render(request, 'main/index.html')


def tasks_report(request):
    return get_tasks_report(request)


def summary_report(request):
    return get_summary_report(request)
