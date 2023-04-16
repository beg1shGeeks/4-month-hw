from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneView, name='phones'),
    path('phones/<int:id>/', views.PhoneDetailView, name='phone_detail'),
]