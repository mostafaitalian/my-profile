from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', TemplateView.as_view(template_name="myprofile/dashboard.html")),
    path('dashboard/', views.dashboard, name="myprofile_dashboard")
]
