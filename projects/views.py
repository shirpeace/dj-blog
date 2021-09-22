from django.shortcuts import render
from projects.models import Project

# Create your views here.
# view function to retrieve all projects
def project_index(request):
    #query - select all projects 
    projects = Project.objects.all()
    
    #dictionary of queryset (result)
    context = {  
        'projects': projects
    }
    #render html page and data dictionary
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    #query - select project where pk=pk (pk is the id field) 
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)