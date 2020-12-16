from django.urls import path
from IIT_OpenOCR import views as iitviews


urlpatterns = [
    path('', iitviews.home ,name='IITB_OpenOCR-Homepage'),
    path('books/',iitviews.bookpage,name='IITB_OpenOCR-Bookspage'),
    path('sets/',iitviews.sets_detail,name='IITB_OpenOCR-Sets'),
    path('users/',iitviews.search_user, name='IITB_OpenOCR-UsersPage'),
    path('users/<str:g_username>/', iitviews.spcific_user, name='IITB_OpenOCR-User'),
    path('about/',iitviews.about,name='IITB_OpenOCR-Aboutpage'),
    path('sets/<str:setid>/',iitviews.assign_user,name='IITB_OpenOCR-AssignUser'),
    path('sets/<str:setid>/<str:github_username>/',iitviews.set_user,name='IITB_OpenOCR-SetUser'),
    path('set_update/<str:setID>/',iitviews.set_update,name='IITB_OpenOCR-SetUpdate'),
    path('saveset/<str:setID>/',iitviews.saveset,name='IITB_OpenOCR-saveset'),
    path('deleteset/<str:setID>/',iitviews.deleteset,name='IITB_OpenOCR-deleteset'),
    path('set_log/<str:setID>/',iitviews.set_log,name='IITB_OpenOCR-SetLog'),
    path('books_update/<str:book_id>/',iitviews.book_update,name='IITB_OpenOCR-BookUpdate'),
    path('savebook/<str:book_id>/',iitviews.savebook,name='IITB_OpenOCR-savebook'),
    path('createset/', iitviews.createnewset, name = 'IITB_OpenOCR-createset'),
    path('savenewset/', iitviews.savenewset, name = 'IITB_OpenOCR-savenewset')
]