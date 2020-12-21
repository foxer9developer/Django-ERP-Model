from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from IIT_OpenOCR.models import users
from .forms import RegisterationForm, loginForm

from django.contrib import messages

# Create your views here.
# def register(request):
#     form = RegisterationForm()
#     if(request.method == 'POST'):
#         form = RegisterationForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect('accounts:login')

#     contents = {'form': form}
#     return render(request, 'register.html', contents)


def loginPage(request):
	return render(request, 'login.html')

def logoutLink(request):
	logout(request)
	return redirect('accounts:login')
