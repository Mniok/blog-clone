from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from authentication.models import AuthenticationPost


def ProfileDefaultPosts(profile_user, page):
    posts_list = AuthenticationPost.objects.filter(author_id=profile_user.id)
    paginator = Paginator(posts_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts