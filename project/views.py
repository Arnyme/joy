from django.shortcuts import render
from .models import Project
# Create your views here.

def view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request,'project.html',{'projects':projects})


def view(request,pk):
    project = Project.objects.filter(pk=pk).get()
    return render(request,'view.html',{'project':project})