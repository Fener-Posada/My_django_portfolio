from django.shortcuts import render, get_object_or_404
#Traer modelo de datos
from .models import projects

def home(request):
    my_projects = projects.objects.all()
    return render(request, 'home.html' , {"my_projects": my_projects} )


def detail_project(request, projects_id):
    my_project = get_object_or_404(projects, pk = projects_id )
    return render (request, 'portfolio-details.html', {'my_project': my_project})