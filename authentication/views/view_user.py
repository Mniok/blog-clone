from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthUser, AuthenticationPost
from ..models import Post

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'signup.html', {"form":form})



@login_required(login_url="/login")
def profile(request, userid):
    user = AuthUser.objects.get(id=userid)
    posts = Post.objects.all()
    
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
            return render(request, 'profile.html')
    else:
        form = PostForm()
    context= {'user':user, 'posts':posts, 'form':form}
    return render(request, 'profile.html', context)