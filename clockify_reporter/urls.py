from django.urls import path
from .views import home, tasks_report, summary_report

urlpatterns = [
    path("", home, name="home"),
    path("tasks_report", tasks_report, name="tasks_report"),
    path("summary_report", summary_report, name="summary_report")
]
