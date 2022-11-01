from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("clockify_reporter.urls")),
    path('tasks_report', include("clockify_reporter.urls")),
    path('summary_report', include("clockify_reporter.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
