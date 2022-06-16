from django.shortcuts import render, redirect

from .services.service_user import ProfileDefaultPosts
from ..forms import RegisterForm, PostForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import User, AuthenticationPost
from ..models import Post
from ..models import AccBlogSettings

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
    profile_user = User.objects.get(id=userid)
    try:
        profile_settings = AccBlogSettings.objects.get(account=profile_user)
    except AccBlogSettings.DoesNotExist:
        profile_settings = None

    # posts = AuthenticationPost.objects.all()
    #posts = AuthenticationPost.objects.filter(author_id=profile_user.id)
    # page = request.GET.get('page', 1)
    # posts_list = AuthenticationPost.objects.filter(author_id=profile_user.id)
    # paginator = Paginator(posts_list, 5)
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    page = request.GET.get('page', 1)
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = AuthenticationPost.objects.filter(id=post_id).first()
        if post and profile_user.id == request.user.id:
            post.delete()
            return redirect('profile', userid=userid)

    else:
        posts = ProfileDefaultPosts(profile_user, page)
    context= {'profile_user':profile_user, 'posts':posts, 'profile_settings':profile_settings}
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
