from django.urls import path
from . import views

app_name = 'group_chat_app'
urlpatterns = [
    path('', views.userlogin, name='userlogin'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userhome/', views.userhome, name='userhome'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adduser/', views.adduser, name='adduser'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('userinfo/<str:username>', views.userinfo, name='userinfo'),
    path('updateuser/<str:username>', views.updateuser, name='updateuser'),
    path('deleteuser/<str:username>', views.deleteuser, name='deleteuser'),
    path('creategroup/<str:username>', views.creategroup, name='creategroup'),
    path('viewgroup/<str:groupname>', views.viewgroup, name='viewgroup'),
    path('removemember/<str:groupname>/<str:username>', views.removemember, name='removemember'),
    path('deletegroup/<str:groupname>/<str:username>', views.deletegroup, name='deletegroup'),
    path('viewgroupmessages/<str:groupname>', views.viewgroupmessages, name='viewgroupmessages'),
    path('like/<int:messageid>', views.like, name='like'),
    path('dislike/<int:messageid>', views.dislike, name='dislike'),
]
