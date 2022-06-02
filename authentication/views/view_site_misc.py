from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#from ..forms import RegisterForm, AuthenticationPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import Post
from ..models import AuthenticationPost, Post, FollowerRequest, AuthUser


# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = AuthenticationPost.objects.exclude(author_id=request.user.id).\
        filter(author__ACCOUNT_ID1__account=request.user.id)
    # if request.method == "POST":
    #     post_id = request.POST.get("post-id")
    #     post = Post.objects#.filter(id=post_id).first()
    #     if post and post.author == request.user:
    #         post.delete()
    return render(request, 'home.html', {"posts": posts})



def TOS_page(request):
    return render(request, 'tos.html')

