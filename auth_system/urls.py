from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns= [
	path('',views.home, name="home"),
	path('register/', views.register, name="register" ),
	path('login/',views.loginpage, name="login"),
	path('success_page/',views.success_page,name="success_page"),
	path('logout/',views.logoutUser, name="logout"),
]