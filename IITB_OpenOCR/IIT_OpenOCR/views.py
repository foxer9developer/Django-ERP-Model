from django.shortcuts import render, redirect, get_object_or_404
from IIT_OpenOCR.models import users, sets
from .models import sets, book
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from github import Github
from django.http import HttpResponse
from .forms import setsform, bookform, newsetsform, AddUserForm
from django.http import QueryDict

# PMusername="TeamOCR-IITB"
PMpass="e3c7d3d67598572c39c93861d56f2c8479b74cce"

@login_required
def home(request):
    if request.user.is_authenticated:
        count = users.objects.filter(github_username = request.user.username).count()
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
        g = Github(access_token)
        g.get_repos
        repo = g.get_repo("TeamOCR-IITB/IITB-ProjectManager")
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
            #<!-- {% if sets.bookid == book.book_id %} --><!-- {% endif %} -->


    else:
        context = {
            'title': 'Books',
            'books': book.objects.all(),
            'sets': sets.objects.all()
            }
    return render(request, 'IIT_OpenOCR/books.html', context)
############################################################################
@login_required
def assign_user(request,setid): #to display the list of correctors/verifiers to assign them to the sets
    clicked_set= sets.objects.get(setID=setid)
    selected_user = request.GET.get('selected')
    searched_user=request.GET.get('searchBar_assigned')
    if(clicked_set.setCorrector):
        if(selected_user=="Available"):
            context = {
            'title': 'Assign Verifier',
            'users': users.objects.filter(user_role="Verifier").filter(user_status="Available"),
            'setid': setid
            }
        elif(selected_user=="Assigned"):
            context = {
                'title': 'Assign Verifier',
                'users': users.objects.filter(user_role="Verifier").filter(user_status="Assigned"),
                'setid': setid
            }
        elif (selected_user == "All"):
            context = {
                'title': 'Assign Verifier',
                'users': users.objects.filter(user_role="Verifier"),
                'setid': setid
            }
        elif searched_user != '' and searched_user is not None:
            context = {
                'title': 'Searched User',
                'users': users.objects.filter(name__icontains=searched_user).filter(user_role="Verifier")
            }
        else:
            context = { 
                'title': 'Assign Verifier',
                'users': users.objects.filter(user_role="Verifier").filter(user_status="Available"),
                'setid': setid
            }

    else:
        if (selected_user == "Available"):
            context = {
            'title':'Assign Corrector',
            'users': users.objects.filter(user_role="Corrector").filter(user_status="Available"),
            'setid': setid
            }
        elif (selected_user == "Assigned"):
            context = {
                'title': 'Assign Corrector',
                'users': users.objects.filter(user_role="Corrector").filter(user_status="Assigned"),
                'setid': setid
            }
        elif (selected_user == "All"):
            context = {
                'title': 'Assign Corrector',
                'users': users.objects.filter(user_role="Corrector"),
                'setid': setid
            }
        elif searched_user != '' and searched_user is not None:
            context = {
                'title': 'Searched User',
                'users': users.objects.filter(name__icontains=searched_user).filter(user_role="Corrector")
            }
        else:
            context = {
                'title': 'Assign Corrector',
                'users': users.objects.filter(user_role="Corrector").filter(user_status="Available"),
                'setid': setid
            }

    return render(request, 'IIT_OpenOCR/assignuser.html',context)
########################################################################################################################
@login_required
def set_user(request,github_username, setid):#setting the user as collaborator
    g = Github(PMpass)
    repos = g.get_repos
    print("user === ",g.get_user())
    clicked_user = users.objects.get(github_username=github_username)
    print("clicked user = ", clicked_user)
    set_toassign = sets.objects.get(setID=setid)
    reponame = set_toassign.repoistoryName
    repo = g.get_repo(reponame)
    if(set_toassign.setCorrector):
        repo.add_to_collaborators(github_username, permission="admin")
        set_toassign.setVerifier = clicked_user
        set_toassign.status = "Verifier"
        print("sent invitation to Verifier")

    else:
        repo.add_to_collaborators(github_username, permission="admin")
        set_toassign.setCorrector =clicked_user
        set_toassign.status = "Corrector"
        print("sent invitation to corrector")
    set_toassign.version = 1
    set_toassign.save()
    clicked_user.user_status = "Assigned"
    clicked_user.save()
    return redirect('/sets')

@login_required
def search_user(request): #Users Page
        selected_role = request.GET.get('userrole')
        selected_status = request.GET.get('userstatus')
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
        elif(selected_status =="All"):
            context = {
                'title':'All Users',
                'users': users.objects.all()
            }
        elif(selected_status =="Available"):
            context = {
                'title': 'Available Users',
                'users': users.objects.filter(user_status="Available")
            }
        elif(selected_status == "Assigned"):
            context = {
                'title': 'Assigned Users',
                'users': users.objects.filter(user_status="Assigned")
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
def adduser(request):
    form = AddUserForm()
    if(request.method == 'POST'):
        form = AddUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/users')

    contents = {'form': form}
    return render(request, 'IIT_OpenOCR/adduser.html', contents)

@login_required
def deleteuser(request, g_username):
    print("wow")
    if request.method == 'POST':
        git_username = users.objects.get(github_username = g_username)
        git_username.delete()
        print("user with username ", git_username, " deleted")
    return redirect('/users')


@login_required
def deletebook(request, book_id):
    if request.method == 'POST':
        specific_book = book.objects.get(book_id = book_id)
        specific_book.delete()
    return redirect('/books')

@login_required
def sets_detail(request): #Sets Page
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

@login_required
def set_update(request, setID): #Update sets page
    clicked_set = sets.objects.get(setID = setID)
    context = {
        'title': 'update-set',
        'sets' : setsform(instance=clicked_set)
    }
    return render(request, 'IIT_OpenOCR/setsUpdate.html', context)

@login_required
def saveset(request, setID): #saving updated sets in the db
    setsID = request.POST.dict()['setID']
    clicked = sets.objects.get(setID=setsID)
    repository = request.POST.dict()['repoistoryName']
    print(repository)
    version = request.POST.dict()['version']
    stage = request.POST.dict()['stage']
    # role = request.GET.get('user_role')
    formobj1 = setsform(request.POST, instance= clicked)
    if formobj1.is_valid():
        formobj1.save()
        g = Github(PMpass)
        user = g.get_user()
        repo = g.get_repo(repository)
        contents = repo.get_contents("project.xml")
        repo.update_file( contents.path,"Project.xml file updated from PMUI.","<?xml version='1.0'?>\n<Project name='Book1'>\n<ItemGroup>\n<Filter Include='Image'>\n<Extensions>jpeg;jpg;png;</Extensions>\n</Filter>\n<Filter Include='Document'>\n<Extensions>docx;txt;html</Extensions>\n</Filter>\n</ItemGroup>\n<ItemGroup>\n</ItemGroup>\n<Metadata>\n<Version>{}</Version>\n<Stage>{}</Stage>\n<Corrector>None</Corrector>\n<SanityChecker>None</SanityChecker>\n<Verifier>None</Verifier>\n</Metadata>\n</Project>".format(version,stage), contents.sha )

    else:
        print("error2 = ",formobj1.errors)
    return redirect('/sets')

@login_required
def deleteset(request, setID):
    if request.method == 'POST':
        setid = sets.objects.get(setID = setID)
        setid.delete()
        print("set with set-id ", setid, " deleted")
    return redirect('/sets')

@login_required
def book_update(request, book_id): #update book page
    clicked_set = book.objects.get(book_id = book_id)
    context = {
        'title': 'update-book',
        'book' : bookform(instance=clicked_set)
    }
    print("Context ended")
    return render(request, 'IIT_OpenOCR/bookupdate.html', context)

@login_required
def savebook(request, book_id): #saving updated book in the db
    bookID = request.POST.dict()['book_id']
    clicked = book.objects.get(book_id=bookID)
    formobj1 = bookform(request.POST, instance= clicked)
    if formobj1.is_valid():
        formobj1.save()
        
    else:
        print("error2 = ",formobj1.errors)
    return redirect('/books')

@login_required
def addbook(request):#Add new book
    if request.method == 'POST': #saving the book in db
        formobj = bookform(request.POST)
        if formobj.is_valid():
            formobj.save()
        else:
            print("form is not valid, error = ", formobj.errors)
        return redirect("/books")
    else: #creating a new form
        formobj = bookform()
        return render(request, 'IIT_OpenOCR/createbook.html', {'book':formobj})
    
@login_required    
def createnewset(request): #create new sets page
    formobj = newsetsform()
    return render(request, 'IIT_OpenOCR/createset.html', {'set':formobj})

@login_required
def savenewset(request): #save new set in db and create a repository for then new set
    if request.method == 'POST':
        formobj = newsetsform(request.POST)
        # print(formobj)
        if formobj.is_valid():
            formobj.save()
            reponame = request.POST.dict()['repoistoryName']
            deadline = request.POST.dict()['vone_deadline']
            # lastdate = request.
            desc = "This is the set for "+ reponame+", The deadline for this is "+ deadline +"."
            # +" Last date to submit is "+ lastdate
            g = Github(PMpass)
            user = g.get_user()
            user.create_repo(name=reponame, description=desc)
        else:
            print("Formobj is not valid...errors = ", formobj.errors)            

    else:
        print("Data not recieved")
    return redirect('/sets')

@login_required
def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})

@login_required
def spcific_user(request, g_username):
    clicked_user = users.objects.get(github_username=g_username)
    clicked_sets = sets.objects.filter(setCorrector=clicked_user)|sets.objects.filter(setVerifier=clicked_user)
    context = {
        'title': g_username,
        'clicked': clicked_user,
        'sets':clicked_sets
    }
    return render(request,'IIT_OpenOCR/specificuser.html',context)

@login_required
def set_log(request, setID):
    clicked_set = sets.objects.filter(setID = setID)
    context = {
        'title' : 'Sets Log Page',
        'sets' : clicked_set
    }
    return render(request, 'IIT_OpenOCR/setslog.html',context)
    

def page_not_found(request, exception):
    return render(request,'IIT_OpenOCR/404.html',status=404)

def server_error(request):
    return render(request,'IIT_OpenOCR/500.html',status=500)

def bad_request(request, exception):
    return render(request,'IIT_OpenOCR/400.html',status=400)

def permission_denied(request, exception):
    return render(request,'IIT_OpenOCR/403.html',status=403)
