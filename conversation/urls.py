from django.urls import path
from . import views




urlpatterns = [
    path('new-chat/<str:pk>/', views.new_conversation, name="new_conversation"),
    path('question/', views.about, name="about"),
    path('detail/', views.detail, name="detail"),
]
