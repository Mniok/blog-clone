#from django.contrib.auth.models import User
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
#from ..forms import PostChooseForm
#from ..forms import RegisterForm, AuthenticationPostForm
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import login, logout, authenticate
#from ..models import AuthenticationPost, Post, FollowerRequest, AuthUser
#from crispy_forms.helper import FormHelper

# Create your views here.
def TOS_page(request):
    return render(request, 'tos.html')

