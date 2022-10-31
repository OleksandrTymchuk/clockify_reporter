from django.urls import path
from .views import home, first_report, second_report

urlpatterns = [
    path("", home, name="home"),
    path("first_report", first_report, name="first_report"),
    path("second_report", second_report, name="second_report")
]
