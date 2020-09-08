from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='IITB_OpenOCR-Homepage'),
    path('about/',views.about,name='IITB_OpenOCR-Aboutpage')
]