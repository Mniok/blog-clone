#from ast import pattern
from django.urls import path
from . import views


urlpatterns =[
    path('', views.view_site_misc.home, name='home'),
    path('home', views.view_site_misc.home, name='home'),
    path('signup', views.view_user.sign_up, name='signup'),
    path('create-post', views.view_post.create_post, name='create-post'),
    path('tos', views.view_site_misc.TOS_page, name='tos'),
    path('profile', views.view_user.profile, name='profile'),
]
