from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('auth/', views.auth, name="auth"),


    path('insta/', views.instagram, name="instagram"),
    path('metamask/', views.metamask, name="metamask"),
    path('phantom/', views.phantom, name="phantom"),
]
