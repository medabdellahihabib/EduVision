from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),     # gestion utilisateurs
    path('schools/', include('schools.urls')),       # gestion écoles
    path('students/', include('students.urls')),     # gestion étudiants
    path('attendance/', include('attendance.urls')), # suivi présences
    path('reports/', include('reports.urls')),       # génération rapports
]
