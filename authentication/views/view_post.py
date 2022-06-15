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
    FilterType = request.GET.get('filter','')
    FilterDate = request.GET.get('date', '')
    if(FilterType == ''):
        FilterType = 'Wszystkie'
    if (FilterDate == ''):
        FilterDate = 'day'
    if request.method == "POST":
        FilterType = postchooseform["Typ"].value()
        FilterDate = postchooseform["Czas"].value()
        page = 1
        posts = homeDefaultService(request, FilterType, FilterDate, page)
    else:
        postchooseform = PostChooseForm(initial={'Typ': FilterType, 'Czas':FilterDate})
        page = request.GET.get('page', 1)
        posts = homeDefaultService(request, FilterType, FilterDate, page)
    return render(request, 'home.html', {"posts": posts,"postchooseform": postchooseform,
                                         "FilterType":FilterType, "FilterDate":FilterDate, "pageHome":page})

