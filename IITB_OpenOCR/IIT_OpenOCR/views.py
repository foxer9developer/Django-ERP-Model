from django.shortcuts import render, redirect
from IIT_OpenOCR.models import users, SetStatus
from .models import sets
from .models import book
from django.contrib import messages
from django.contrib.auth import logout
from github import Github
from django.http import HttpResponse


def books(request):
    if request.user.is_authenticated:
        count = users.objects.filter(github_username = request.user.username).count()
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
        g = Github(access_token)
        g.get_repos
        repo = g.get_repo("svtsanoj/Open-OCR-Correct")
        contents = repo.get_contents("README.md")
        print(contents)
        if(count != 1):
            logout(request)
            messages.info(request, 'This account is not registered to Akshar Anveshini. Please Register with to Continue')
            return redirect('/register')
    else:
        return redirect('/login')

    context = {
        'title':'Books',
        'books': book.objects.all()
            }
    return render(request,'IIT_OpenOCR/home.html',context)

def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})

def spcific_user(request):
    context = {
        'title':'user101'
    }
    return render(request,'IIT_OpenOCR/specificuser.html',context)

def assign_user(request):
    return HttpResponse("AssignUser Page")

def search_user(request):
    context = {
        'title':'Users',
        'users': users.objects.all()
    }
    return render(request,'IIT_OpenOCR/userspage.html', context)

def sets_detail(request):
    context = {
        'title':'Sets',
        'sets': sets.objects.all()
            }
    return render(request,'IIT_OpenOCR/Sets.html', context)

def book_update(request):
    return HttpResponse("Book Update")

def set_log(request):
    return HttpResponse("set log")

def set_update(request):
    return HttpResponse("Set Update")
