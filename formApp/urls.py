from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='claim-home'),
    path('history/', views.history, name='claim-history'),
    path('history/user<int:user_pk>/claim<int:claim_pk>', views.editClaim, name='claim-edit'),
    path('login/', views.login, name='claim-login'),
    path('signup/', views.signup, name='claim-signup'),
    path('logout/', LogoutView.as_view(), name='claim-logout')
]