from django.shortcuts import render
from projects.models import Project_inv, Project_inv3

# Create your views here.

def project_index(request):
    projects = Project_inv3.objects.all()
    context = {'projects':projects}
    for project in projects:
        temp_var = 'images/'+str(project.image)
        project.image = temp_var
        print(project.image)

    return render(request,'project_index.html',context)

def project_detail(request,pk):
    project = Project_inv3.objects.get(pk=pk)
    context = {
        'project':project
    }
    return render(request,'project_detail.html',context)
