from django.shortcuts import render, redirect
from .models import users, SetStatus
from django.contrib import messages
from django.contrib.auth import logout
from github import Github


def home(request):
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
        'users': users.objects.all()
            }
    return render(request,'IIT_OpenOCR/home.html',context)

def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})
