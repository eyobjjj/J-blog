from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('auth/', views.auth, name="auth"),


    path('insta/', views.instagram, name="instagram"),
    path('e-tiktok1/', views.e_tiktok1, name="e-tiktok1"),
]
