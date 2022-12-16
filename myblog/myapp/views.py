from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-published_date')
	return render(request, 'index.html', {'posts':posts})

def about(request):
	return render(request, 'about.html', {})

def post(request, id):
	post = Post.objects.get(pk = id)
	print(post)
	return render(request, 'post.html', {'post':post})

def contact(request):
	return render(request, 'contact.html', {})

def newpost(request):
	if request.method  == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm()

	return render(request, 'newpost.html', {'form':form})

def post_edit(request, id):
	pst = Post.objects.get(pk = id)
	if request.method =='POST':
		form = PostForm(request.POST, instance = pst)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm(instance = pst)
	return render(request, 'postedit.html', {'form':form})

def post_delete(request, id):
	usr = Post.objects.get(id = id)
	usr.delete()
	return redirect('/')
	
#worked
def registerUser(request):
	if request.user.is_authenticated:
		return redirect("/")
	frm = UserCreationForm()
	print(frm)

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	frm = UserCreationForm()
	return render (request=request, template_name="registration/register.html", context={"frm":frm})

	#return render(request, 'register.html', {'frm':frm})



# def login_request(request):
# 	print(request)
# 	# if request.user.is_authenticated:
# 	# 	print("logined")
# 	# 	return redirect('index')
# 	print("start")
# 	if request.method == "POST":
# 		print("start1")
# 		frm  = AuthenticationForm(request.POST)
# 		print("Level 1")
# 		if frm.is_valid():
# 			print("Level 2")
# 			user  = frm.save()
# 			login(request, user)
# 			print("ssss")
# 			return redirect('index')
# 	frm = AuthenticationForm()
# 	print("ssss88")
# 	return render (request=request, template_name="registration/login.html", context={"frm":frm})


def logoutUser(request):
	logout(request)
	return redirect("/")


	