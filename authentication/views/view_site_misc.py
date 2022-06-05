#from django.contrib.auth.models import User
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from ..forms import PostChooseForm
#from ..forms import RegisterForm, AuthenticationPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
#from ..models import AuthenticationPost, Post, FollowerRequest, AuthUser
from crispy_forms.helper import FormHelper
from .services.service_site_misc import *

# Create your views here.
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

def TOS_page(request):
    return render(request, 'tos.html')

