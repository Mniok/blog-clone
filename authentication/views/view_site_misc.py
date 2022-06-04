from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from ..forms import PostChooseForm
#from ..forms import RegisterForm, AuthenticationPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost, Post, FollowerRequest, AuthUser
from crispy_forms.helper import FormHelper

# Create your views here.
@login_required(login_url='/login')
def home(request):
    postchooseform = PostChooseForm(request.POST)
    if request.method == "POST":
        choosen = postchooseform["Typ"].value()
        if choosen == "Obserwowani":
            posts_list = AuthenticationPost.objects.exclude(author_id=request.user.id). \
                filter(author__ACCOUNT_ID1__account=request.user.id)
        if choosen == "Wszystkie":
            posts_list = posts = AuthenticationPost.objects.all()
    else:
        #form = PostForm()
        # posts = AuthenticationPost.objects.exclude(author_id=request.user.id).\
        # filter(author__ACCOUNT_ID1__account=request.user.id)
        posts_list = AuthenticationPost.objects.all().exclude(author_id=request.user.id)
    # if request.method == "POST":
    #     post_id = request.POST.get("post-id")
    #     post = Post.objects#.filter(id=post_id).first()
    #     if post and post.author == request.user:
    #         post.delete()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {"posts": posts,"postchooseform": postchooseform })



def TOS_page(request):
    return render(request, 'tos.html')

