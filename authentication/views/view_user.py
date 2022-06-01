from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost
from ..models import Post
from ..models import AccBlogSettings
from ..models import AuthUser

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            acc = AccBlogSettings(account=request.user, is_private=0,
                                  profile_background_colour="#ffffff",
                                  tos_accepted=1, window_colour="#ffffff",
                                  border_colour="#ffffff")
            acc.save()
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'signup.html', {"form":form})



@login_required(login_url="/login")
def profile(request):
    posts_profile = AuthenticationPost.objects.filter(author=request.user.id)
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        delete_post = AuthenticationPost.objects.filter(id=post_id)
        if posts_profile:# and delete_post.author == request.user:
            delete_post.delete()
            return redirect('/profile')

    # else:
    #     posts_profile = PostForm()
    return render(request, 'profile.html', {'posts_profile': posts_profile})
