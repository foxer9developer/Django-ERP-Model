from django.shortcuts import render, redirect
from IIT_OpenOCR.models import users, SetStatus,sets
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
    query_bookName = request.GET.get('searchBar_book')
    if(bstatus=="Completed"):
        context = {
            'title': 'CompletedBooks',
            'books': book.objects.filter(book_status="completed"),
            'sets': sets.objects.all()
        }
    elif (bstatus == "InProgress"):
        context = {
            'title': 'BooksInProgress',
            'books': book.objects.filter(book_status="In Progress"),
            'sets': sets.objects.all()
            }
    elif (bstatus == "All"):
        context = {
            'title': 'Books',
            'books': book.objects.all(),
            'sets': sets.objects.all()
            }
    elif (bstatus == "Unassigned"):
        context = {
            'title': 'Books',
            'books': book.objects.filter(book_status="Unassigned"),
            'sets': sets.objects.all()
            }
    elif (query_bookName != '' and query_bookName is not None):
        context = {
            'title': 'Searched books',
            'books': book.objects.filter(book_name__icontains=query_bookName),
            'sets': sets.objects.all()
            }
    elif (query_bookName != '' and query_bookName is not None):
        context = {
            'title': 'Searched books',
            'books': book.objects.filter(book_name__icontains=query_bookName),
            'sets': sets.objects.all()
            }
    else:
        context = {
            'title': 'Books',
            'books': book.objects.all(),
            'sets': sets.objects.all()
            }
    return render(request, 'IIT_OpenOCR/books.html', context)

@login_required
def assign_user(request):
    return HttpResponse("Develop")

@login_required
def search_user(request):
        selected_role = request.GET.get('userrole')
        query_userName = request.GET.get('searchBar_user')
        if(selected_role == "Corrector"):
            context = {
                 'title': 'Corrector',
                 'users': users.objects.filter(user_role="Corrector")
            }
        elif(selected_role == "Verifier"):
            context = {
                 'title': 'Verifier',
                 'users': users.objects.filter(user_role="Verifier")
            }
        elif (selected_role == "All"):
            context = {
                'title': 'Users',
                'users': users.objects.all()
            }
        elif query_userName != '' and query_userName is not None:
            context = {
                'title': 'Searched User',
                'users': users.objects.filter(name__icontains=query_userName)
            }
        else:
            context = {
                'title': 'Users',
                'users': users.objects.all()
            }
        return render(request, 'IIT_OpenOCR/userspage.html', context)

@login_required
def set_update(request):
    context = {
        'title': 'update'
    }
    return render(request, 'IIT_OpenOCR/setsUpdate.html', context)

@login_required
def sets_detail(request):
    query_book_setspage = request.GET.get('searchBar_book_setspage')
    if query_book_setspage != '' and query_book_setspage is not None:
        context = {
            'title': 'Searching Book in Sets',
            'sets': sets.objects.filter(bookid__book_name__icontains=query_book_setspage)
        }
    else:
        context = {
            'title': 'Sets',
            'sets': sets.objects.all()
        }
    return render(request, 'IIT_OpenOCR/Sets.html', context)


#development
def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})

@login_required
def spcific_user(request, g_username):
    clicked_user = users.objects.get(github_username=g_username)
    clicked_sets = sets.objects.filter(setCorrector=clicked_user)|sets.objects.filter(setVerifier=clicked_user)
    books= book.objects.filter()
    #fetch clicked user
    context = {
        'title': g_username,
        'clicked': clicked_user,
        'sets':clicked_sets
    }
    return render(request,'IIT_OpenOCR/specificuser.html',context)


def book_update(request):
    return HttpResponse("Book Update")

def set_log(request):
    return HttpResponse("set log")


