from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
	return render(request, 'auth_system/index.html')


def register(request):
	
	form= CreateUserForm()
	if request.method=='POST':
		form= CreateUserForm(request.POST)
		if form.is_valid():
			ty=request.POST.getlist('check')
			print(ty)
			user= form.save()
			
			username=form.cleaned_data.get('username')
			
			
			messages.success(request, 'Account was created for ' + username)


			return redirect('login')
	context={'form':form}
	return render(request, 'auth_system/register.html',context)


def loginpage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user= authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('success_page')
			
			
		else:
			messages.info(request,'Username OR password is incorrect')
	return render(request, 'auth_system/login.html')

def success_page(request):
	return render(request,'auth_system/success_page.html')

def logoutUser(request):
	logout(request)
	return redirect('home')
