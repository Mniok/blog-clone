from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost, Post


# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'home.html', {"posts": posts})



def TOS_page(request):
    form = PostForm()
    return render(request, 'tos.html', {'form': form})

