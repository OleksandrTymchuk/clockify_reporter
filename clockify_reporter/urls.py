from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('first_report', include("main.urls")),
    path('second_report', include("main.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
