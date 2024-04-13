from django.shortcuts import render
from project.models import Project
from client.models import Client
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from member.models import Member
from validate_email import validate_email
def index(request):
    projects = Project.objects.all().order_by('-created_at')[0:5]
    clients = Client.objects.all()
    
    context = {
        'clients':clients,
        'projects':projects
    }
    return render(request,'index.html',context)


def register(request):
    return render(request,'auth/register.html')

@csrf_exempt
def member_save(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
            # if validate_email(email):
            # if(Member.objects.filter(email=email).exists()):
            #         messages.error(request,"your email already existing ")
            #         return render(request,'auth/register.html',{'first_name':email})
        
        # else:
        #     if not str.isalpha(first_name) :
        #         messages.error(request,"must be characters")
        #         return render(request,'auth/register.html',{'first_name':first_name})
        
               
    return render(request,'auth/register.html',{'first_name':first_name})
        
def login(request):
    return render(request,'auth/login.html')