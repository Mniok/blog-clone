from django.shortcuts import render, redirect

from .services.service_follower import FollowersDefault
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
    followers = FollowersDefault(request)
    if request.method == "POST":
        follower_id = request.POST.get("follower-id")
        delete_follower = FollowerRequest.objects.filter(account_id1=follower_id)
        delete_follower.delete()
        return redirect('/followers')
    return render(request, 'followers.html', {'followers': followers})



