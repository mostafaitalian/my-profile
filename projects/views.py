from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()

    return render(request, 'projects/project_index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, {'id': pk})

    return render(request, 'projects/project_detail.html', {'project': project})