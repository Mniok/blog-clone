from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm, PostChooseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
#from ..models import AuthenticationPost
#from ..models import AuthUser
#from ..models import Post, PostSettings
from .services.service_post import *


# Create your views here.
@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            createPostService(request, form)
            return redirect("/home")

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})




@login_required(login_url='/login')
def home(request):
    postchooseform = PostChooseForm(request.POST)
    if request.method == "POST":
        choosen = postchooseform["Typ"].value()
        if choosen == "Obserwowani":
            return redirect('/home/following')
        if choosen == "Wszystkie":
            return redirect('/home')
    posts = homeDefaultService(request)
    return render(request, 'home.html', {"posts": posts,"postchooseform": postchooseform })

@login_required(login_url='/login')
def homeFollowing(request):
    postchooseform = PostChooseForm(request.POST)
    if request.method == "POST":
        choosen = postchooseform["Typ"].value()
        if choosen == "Obserwowani":
            return redirect('/home/following')
        if choosen == "Wszystkie":
            return redirect('/home')
    posts = homeFollowingService(request)
    return render(request, 'home/following.html', {"posts": posts, "postchooseform": postchooseform})
