
from django.urls import path
from generator_app import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('get_password', views.password, name="password"),
    path('about', views.about_me, name="about_me")
]
