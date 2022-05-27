from django.shortcuts import render, redirect
from ..forms import RegisterForm, PostForm, FollowerRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost
from ..models import FollowerRequest
from ..models import AuthUser
#tutaj model post nie bedzie potrzebny tylko user i followers, ale na razie zmagam sie z migracja i jeszcze nie ma nic importowalnego xD


# Create your views here.
@login_required(login_url='/login')
def followers_page(request):
    followers = FollowerRequest.objects.all().filter(account=5, request_accepted=1)
    return render(request, 'followers.html', {'followers': followers})

# @login_required(login_url='/login')
# def home(request):
#     posts = AuthenticationPost.objects.all()
#     if request.method == "POST":
#         post_id = request.POST.get("post-id")
#         post = AuthenticationPost.objects.filter(id=post_id).first()
#         if post and post.author == request.user:
#             post.delete()
#     return render(request, 'home.html', {"posts": posts})

#formularz do zdefiniowanaia w forms.py
