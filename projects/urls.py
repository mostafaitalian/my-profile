from django.urls import path
from . import views

app_name='projects'

urlpatterns = [
    path('', views.index, name="project_list"),
    path('project/<int:pk>/', views.project_detail, name='project_detail')
]
