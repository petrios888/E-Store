from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

#login_required	
def userProfile(request):
	user = request.user
	context = {'user': user }
	template = 'profile.html'
	return render(request,template,context)
	
	
	
def Aleph(request):
	context = locals()
	template = 'Aleph.html'
	return render(request,template,context)
	
	
	
def Beth(request):
	context = locals()
	template = 'Beth.html'
	return render(request,template,context)

	
	
	
	
	
# Create your views here.
