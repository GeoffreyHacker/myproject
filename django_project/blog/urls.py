from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('service/', views.service, name="servece",),
    path('poem/', views.poems, name="poems")
]