from django.urls import path
from . import views


app_name = 'mysite'

urlpatterns = [
    path('create/', views.CreateSiteView.as_view(), name='mysite_create')
]
