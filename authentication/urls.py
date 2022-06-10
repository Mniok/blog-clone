#from ast import pattern
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('', views.view_post.home, name='home'),
    path('home', views.view_post.home, name='home'),
    path('home/following', views.view_post.homeFollowing, name='homeFollowing'),
    path('signup', views.view_user.sign_up, name='signup'),
    path('create-post', views.view_post.create_post, name='create-post'),
    path('tos', views.view_site_misc.TOS_page, name='tos'),
    path('profile/<str:userid>', views.view_user.profile, name='profile'),
    path('followers', views.view_follower.followers_page, name='followers'),
    path('edit-profile', views.view_user.edit_profile, name='edit-profile'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),

]
