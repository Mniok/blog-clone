from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost
from ..models import AuthUser
from ..models import Post, PostSettings

# Create your views here.
@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            post_set = PostSettings(post_id=post.id, is_private=0, comments_blocked=0)
            post_set.save()
            return redirect("/home")

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

