from django.urls import path
from . import views


urlpatterns = [
    path('', views.books ,name='IITB_OpenOCR-Bookspage'),
    path('book_update/',views.book_update,name='IITB_OpenOCR-BookUpdate'),
    path('sets/',views.sets_detail,name='IITB_OpenOCR-Sets'),
    path('users/',views.search_user, name='IITB_OpenOCR-UsersPage'),
    path('users/user101/', views.spcific_user, name='IITB_OpenOCR-User'),
    path('about/',views.about,name='IITB_OpenOCR-Aboutpage'),
    path('sets/assignuser/',views.assign_user,name='IITB_OpenOCR-AssignUser'),
    path('sets/set_update/',views.set_update,name='IITB_OpenOCR-SetUpdate'),
    path('sets/set_log/',views.set_log,name='IITB_OpenOCR-SetLog')
]