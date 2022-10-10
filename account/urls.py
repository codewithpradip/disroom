from django.urls import path
from . import views

urlpatterns = [
    path('user-login/', views.user_login_view, name='user_login'),
    path('user-logout/', views.user_logout_view, name='user_logout'),
]