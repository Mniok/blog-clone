from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthUser, AuthenticationPost
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
                                  #tos_accepted zmieniane z True na 1, żeby zmieściło się w polu 1-znakowym w bazie danych. W tym miejscu może mieć tylko wartość True, bo zaznaczenie jest wymagane do przesłania formularza.
            acc.save()
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




@login_required(login_url="/login") #edycja profilu - work in progress
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm()
    
    return render(request, 'profile_edit.html', {"form":form})
