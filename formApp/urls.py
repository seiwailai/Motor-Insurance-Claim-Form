from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='claim-home'),
    path('history/', views.history, name='claim-history'),
    path('history/<int:pk>', views.editClaim, name='claim-edit')
]