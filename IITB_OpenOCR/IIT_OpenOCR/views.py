from django.shortcuts import render
from .models import users
def home(request):
    context = {
        'users': users.objects.all()
            }
    return render(request,'IIT_OpenOCR/home.html',context)

def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})
