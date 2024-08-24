from django.shortcuts import render, redirect
from .models import User
from .form import UserForm

def index(request):
	user = User.objects.all()
	return render(request, 'index.html', {'user': user})

def login(request):

	return render(request, 'login.html')

def checklogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = User.objects.all()
	for x in user:
		if x.username == username and x.password == password:
			return render(request, 'success.html')
	return redirect('/login')

