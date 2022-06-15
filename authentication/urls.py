#from ast import pattern
from django.urls import path
from . import views


urlpatterns =[
    path('', views.view_post.home, name='home'),
    path('home', views.view_post.home, name='home'),
    path('signup', views.view_user.sign_up, name='signup'),
    path('create-post', views.view_post.create_post, name='create-post'),
    path('tos', views.view_site_misc.TOS_page, name='tos'),
    path('profile/<str:userid>', views.view_user.profile, name='profile'),
    path('followers', views.view_follower.followers_page, name='followers'),
    path('edit-profile', views.view_user.edit_profile, name='edit-profile'),
    path('post/<str:post_id>', views.view_post.post_full, name='post'),
]
