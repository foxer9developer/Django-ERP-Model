from django.urls import path
from IIT_OpenOCR import views as iitviews


urlpatterns = [
    path('', iitviews.home ,name='IITB_OpenOCR-Homepage'),
    path('books/',iitviews.bookpage,name='IITB_OpenOCR-Bookspage'),
    path('book_update/',iitviews.book_update,name='IITB_OpenOCR-BookUpdate'),
    path('sets/',iitviews.sets_detail,name='IITB_OpenOCR-Sets'),
    path('users/',iitviews.search_user, name='IITB_OpenOCR-UsersPage'),
    path('users/<str:g_username>/', iitviews.spcific_user, name='IITB_OpenOCR-User'),
    path('about/',iitviews.about,name='IITB_OpenOCR-Aboutpage'),
    path('sets/<str:setid>/',iitviews.assign_user,name='IITB_OpenOCR-AssignUser'),
    path('sets/<str:setid>/<str:github_username>/',iitviews.set_user,name='IITB_OpenOCR-SetUser'),
    path('sets/set_update/',iitviews.set_update,name='IITB_OpenOCR-SetUpdate'),
    path('sets/set_log/',iitviews.set_log,name='IITB_OpenOCR-SetLog')
]
