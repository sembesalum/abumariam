from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zanzibar/', views.zanzibar, name="zanzibar"),
    path('half-day/', views.half_day, name="half_day"),
    path('full-day/', views.full_day, name="full_day"),
    path('holiday-ideas/', views.holiday_ideas, name="holiday_ideas"),
    path('images/', views.images, name="images"),
    path('videos/', views.videos, name="videos"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('parliament/', views.parliament, name="parliament"),
    path('discovered_paradise/', views.discovered_paradise, name="discovered_paradise"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('request/', views.request, name="request"),

    
    path('half-day-book-form/', views.book_form, name="book_form"),
    path('full-day-book-form/', views.book_form2, name="book_form2"),
    path('holiday-ideas-book-form/', views.book_form3, name="book_form3"),
    path('not_found/', views.not_found, name="not_found"),

    path('leisure-activities/', views.leisure_activities, name="leisure_activities"),
]
