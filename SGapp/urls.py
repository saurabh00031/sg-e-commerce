from django.urls import path
from SGapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [

      path('',views.indox,name="home"),
      path('about_us/',views.about_Us,name="about_us"),
      path('about_pro/',views.about_Pro,name="about_pro"),
      path('services/',views.services,name="services"),
      path('reg_user/', views.UsrView.as_view(), name="reg_user"),
      path('reg_mentor/', views.MentorView.as_view(), name="reg_mentor"),
      path('sgin_user/',views.sgin_user,name="sgin_user"),
      path('sgin_mentor/',views.sgin_mentor,name="sgin_mentor"),
      path('sginpg_mentor/',views.sginpg_mentor,name="sginpg_mentorx"),
      path('sginpg_user/',views.sginpg_user,name="sginpg_user"),
      path('logout_x/',views.logout_x,name="logout_x"),
      path('profile_x/',views.profile_x,name="profile_x"),
      path('sgin_pg_shift/',views.shift,name="sgin_pg_shift"),
      path('search/', views.search, name="search"),
      path('search2/', views.search2, name="search2"),
      path('gov_nov_x/',views.gov_nov_x,name="gov_nov_x"),
      path('request_mentor/<int:id>/',views.request_mentor,name="request_mentor"),
      path('blog/', views.index, name = 'index'),
      path('<str:slug>', views.blog_detailView, name = 'blog_detail'),
      path('addPost/' , views.addPost,name="addPost" ),   
      path('my_posts/',views.my_posts,name="my_posts")
]
    