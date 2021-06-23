from django.shortcuts import render
from django.views.generic import CreateView
from .models import MySite
from .forms import MySiteForm
# Create your views here.


class CreateSiteView(CreateView):
    model = MySite
    form_class = MySiteForm
    template_name = 'mysite/create_site.html'
