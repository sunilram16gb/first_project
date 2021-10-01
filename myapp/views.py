from myapp.models import Post, Profile
from os import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from . models import Profile,Post
def Login_page(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			 login(request,user)
			 return redirect('home')
		else:
			return redirect('login')
	else:
		if not request.user.is_anonymous:
			return redirect('home')
		else:
			return render(request,'index.html')
def home(request):
	if request.user.is_authenticated:
		user=request.user
		name=user.first_name+' '+user.last_name
		pro=Profile.objects.get(user=user)
		pos=Post.objects.filter(user=user)
		context ={'name':name,
		'pro':pro,
		'pos':pos}
		return render(request,'home.html',context)
	else:
		return redirect('login')


def profile(request):
	if request.user.is_authenticated:
		pro=Profile.objects.get(user=request.user)
		pos = Post.objects.filter(user=request.user)
		return render(request,'profile.html',{'pro':pro,'pos':pos})
	else:
		return redirect('login')
def Logout(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('login')

def register(request):
	if request.method=='POST':
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']

		if password1==password2:
			user =User.objects.create(username=username)
			user.set_password(password2)
			user.save()
			return redirect('login')
		else:
			return redirect('login')
	else:
		return redirect('login')



def create_post(request):

	if request.method=='POST':
		user = request.user
		content = request.POST['content']
		p = Post.objects.create(user=user,post=content)
		p.save()
		return redirect('home')
	else:
		return redirect('home')


def edit_profile(request):
	if request.method=='POST':
		user = request.user
		status = request.POST['status']
		loc = request.POST['location']
		p = Profile.objects.get(user=user)
		p.status = status
		p.location = loc
		p.save()
		return redirect('profile')
	else:
		return redirect('profile')
