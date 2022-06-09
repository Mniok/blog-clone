from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.shortcuts import render, redirect
from ...forms import PostChooseForm
#from ..forms import RegisterForm, AuthenticationPostForm
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import login, logout, authenticate
from ...models import AuthenticationPost, Post, FollowerRequest, AuthUser, PostSettings
from crispy_forms.helper import FormHelper


def createPostService(request, form):
    post = form.save(commit = False)
    post.author = request.user
    post.save()
    post_set = PostSettings(post_id=post.id, is_private=0, comments_blocked=0)
    post_set.save()
    return 1





def homeDefaultService(request):
    posts_list = AuthenticationPost.objects.all().exclude(author_id=request.user.id)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts


def homeFollowingService(request):
    postchooseform = PostChooseForm(initial={'Typ':'Obserwowani'})
    posts_list = AuthenticationPost.objects.exclude(author_id=request.user.id). \
        filter(author__ACCOUNT_ID1__account=request.user.id)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts
