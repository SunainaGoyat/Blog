from django.urls import path
# from .views import *
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
	path('', views.index, name = "index"),
	path('about/', views.about, name = "about"),
	path('post/<int:id>', views.post, name = "post"),
	path('contact/', views.contact, name = "contact"),
	path('newpost/', views.newpost, name = "newpost"),
	path('post_edit/<int:id>', views.post_edit, name = "post_edit"),
	path('post_delete/<int:id>', views.post_delete, name = "post_delete"),
	path('register/', views.registerUser, name = "register"),
	path('login/',LoginView.as_view(), name = "login"),
	path('logout/', LogoutView.as_view(next_page='/') , name = "logout"),


]