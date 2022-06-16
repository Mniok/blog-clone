from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from authentication.models import FollowerRequest


def FollowersDefault(request):
    followers_list = FollowerRequest.objects.all().filter(account=request.user.id, request_accepted=1).order_by('account_id1__username')
    page = request.GET.get('page', 1)
    paginator = Paginator(followers_list, 5)
    try:
        followers = paginator.page(page)
    except PageNotAnInteger:
        followers = paginator.page(1)
    except EmptyPage:
        followers = paginator.page(paginator.num_pages)
    return followers