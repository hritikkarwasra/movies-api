from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/movies')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('/')	
	return render(request, 'user/login.html')

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('/')

def register_user(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# print('hi', username, password)
			messages.success(request, ("Registration Successful!"))
			return redirect('/')
			# user = authenticate(username=username, password=password)
			# login(request, user)
		if form.has_error:
			error_message = form.errors
			print(error_message)
			messages.success(request, (error_message))
			return redirect('/register')
	else:
		form = CreateUserForm()

	return render(request, 'user/register.html', {
		'form':form,
		})