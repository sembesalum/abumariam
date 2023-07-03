from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zanzibar/', views.zanzibar, name="zanzibar"),
    path('half_day/', views.half_day, name="half_day"),
    path('full_day/', views.full_day, name="full_day"),
    path('holiday_ideas/', views.holiday_ideas, name="holiday_ideas"),
    path('images/', views.images, name="images"),
    path('videos/', views.videos, name="videos"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('leisure_activities/', views.leisure_activities, name="leisure_activities"),
]
