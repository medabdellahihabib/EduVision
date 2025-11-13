from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # path('', views.ListView.as_view(), name='list'),      # page liste étudiants
    # path('create/', views.CreateView.as_view(), name='create'),  # créer étudiant
]
