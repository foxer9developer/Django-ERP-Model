from django.shortcuts import render, redirect
from IIT_OpenOCR.models import users, SetStatus
from .models import sets
from .models import book
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from github import Github
from django.http import HttpResponse

@login_required
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
        'title': 'Home'
    }
    return render(request,'IIT_OpenOCR/home.html',context)

@login_required
def bookpage(request):
    bstatus = request.GET.get('bookStatus')
    if(bstatus=="Completed"):
        context = {
            'title': 'CompletedBooks',
            'books': book.objects.filter(book_status="completed")
        }
        return render(request, 'IIT_OpenOCR/books.html', context)
    elif (bstatus == "InProgress"):
        context = {
            'title': 'BooksInProgress',
            'books': book.objects.filter(book_status="In Progress")
        }
        return render(request, 'IIT_OpenOCR/books.html', context)
    elif (bstatus == "All"):
        context = {
        'title': 'Books',
        'books': book.objects.all()
        }
        return render(request,'IIT_OpenOCR/books.html',context)
    elif (bstatus == "Unassigned"):
        context = {
        'title': 'Books',
        'books': book.objects.filter(book_status="Unassigned")
        }
        return render(request,'IIT_OpenOCR/books.html',context)
    else:
        context = {
            'title': 'Books',
            'books': book.objects.all()
        }
        return render(request, 'IIT_OpenOCR/books.html', context)



@login_required
def assign_user(request):
    return HttpResponse("AssignUser Page")

@login_required
def search_user(request):
        selected_role = request.GET.get('userrole')
        if(selected_role == "Corrector"):
            context = {
                 'title': 'Corrector',
                 'users': users.objects.filter(user_role="Corrector")
            }
            return render(request, 'IIT_OpenOCR/userspage.html', context)
        elif(selected_role == "Verifier"):
            context = {
                 'title': 'Verifier',
                 'users': users.objects.filter(user_role="Verifier")
            }
            return render(request, 'IIT_OpenOCR/userspage.html', context)
        elif (selected_role == "All"):
            context = {
                'title': 'Users',
                'users': users.objects.all()
            }
            return render(request, 'IIT_OpenOCR/userspage.html', context)
        else:
            context = {
            'title':'Users',
            'users': users.objects.all()
            }
            return render(request,'IIT_OpenOCR/userspage.html', context)

@login_required
def set_update(request):
    context = {
        'title': 'update'
    }
    return render(request, 'IIT_OpenOCR/setsUpdate.html', context)

@login_required
def sets_detail(request):
    context = {
        'title':'Sets',
        'sets': sets.objects.all()
            }
    return render(request,'IIT_OpenOCR/Sets.html', context)


#development
def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})

@login_required
def spcific_user(request):
    context = {
        'title':'user101'
    }
    return render(request,'IIT_OpenOCR/specificuser.html',context)

def book_update(request):
    return HttpResponse("Book Update")

def set_log(request):
    return HttpResponse("set log")


