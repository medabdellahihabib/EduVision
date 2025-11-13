from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),
    path('schools/', include('schools.urls')),
    path('students/', include('students.urls')),
    path('attendance/', include('attendance.urls')),
    path('reports/', include('reports.urls')),
]