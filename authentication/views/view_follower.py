from django.shortcuts import render, redirect

from .services.service_follower import FollowersDefault
from ..forms import RegisterForm, PostForm, FollowerRequestForm, PostChooseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from ..models import AuthenticationPost
from ..models import FollowerRequest
from ..models import AuthUser
#tutaj model post nie bedzie potrzebny tylko user i followers, ale na razie zmagam sie z migracja i jeszcze nie ma nic importowalnego xD


# Create your views here.
@login_required(login_url='/login')
def followers_page(request):
    followerChooseForm = FollowerRequestForm(request.POST)
    page = request.GET.get('page', 1)
    FilterType = request.GET.get('filter','')
    if (FilterType==''):
        FilterType='received'
    followers = FollowersDefault(request, page, FilterType)
    FollowerRequestForm(initial={'zaproszenia': FilterType})
    if request.method == "POST":
        if 'zaproszenia' in request.POST:
            FilterType = followerChooseForm["zaproszenia"].value()
        if 'follower-id' in request.POST:
            follower_id = request.POST.get("follower-id")
            delete_follower = FollowerRequest.objects.filter(account_id1=follower_id, account=request.user.id)
            delete_follower.delete()
        if 'follower-id-rec-rej' in request.POST:
            follower_id = request.POST.get("follower-id-rec-rej")
            delete_follower = FollowerRequest.objects.filter(account_id1=request.user.id, account=follower_id)
            delete_follower.delete()
        if 'follower-id-rec-acc' in request.POST:
            follower_id = request.POST.get("follower-id-rec-acc")
            accept_follower = FollowerRequest.objects.filter(account_id1=request.user.id, account=follower_id)
            accept_follower.update(request_accepted=1)
        page=1
        FollowerRequestForm(initial={'zaproszenia': FilterType})
        followers = FollowersDefault(request, page, FilterType)

    followerChooseForm = FollowerRequestForm(initial={'zaproszenia': FilterType})
    return render(request, 'followers.html', {'followers': followers, "followerChooseForm":followerChooseForm,
                                              'FilterType':FilterType, 'pageFollower':page})



