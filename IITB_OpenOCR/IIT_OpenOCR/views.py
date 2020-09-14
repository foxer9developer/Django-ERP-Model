from django.shortcuts import render, redirect
from .models import users, SetStatus
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        count = users.objects.filter(github_username = request.user.username).count()
        if(count != 1):
            logout(request)
            messages.info(request, 'This account is not registered to Akshar Anveshini. Please Register with to Continue')
            return redirect('/register')
    else:
        return redirect('/login')

    # usersObjects = users.objects.all()
    # setStatusObjects = SetStatus.objects.all()
    # for user in usersObjects:
    #     if(user['user_role']!="Project Manager"):
    #         for i, setstatus in enumerate(setStatusObjects):
    #             if (setstatus['github_username'] == user['github_username']):
    #                 usersObjects[user['sets_completed']] = setstatus['sets_completed']
    #                 usersObjects[user['pages_completed']] = setstatus['pages_completed']
    #                 usersObjects[user['avg_rating']] = setstatus['avg_rating']
    #                 del setStatusObjects[i]
    #                 break
    context = {
        'users': users.objects.all()
            }
    return render(request,'IIT_OpenOCR/home.html',context)

def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})
