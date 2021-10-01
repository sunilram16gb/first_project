from django.urls import path
from . import views

urlpatterns=[
    path('',views.Login_page,name='login'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('register',views.register,name='register'),
    path('create_post',views.create_post,name='create_post'),
    path('edit_profile',views.edit_profile,name='edit'),
]
