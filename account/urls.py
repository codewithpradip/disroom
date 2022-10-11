from django.urls import path
from . import views

urlpatterns = [
    path('user-login/', views.user_login_view, name='user_login'),
    path('user-logout/', views.user_logout_view, name='user_logout'),
    path('user-register/', views.user_register_view, name='user_register'),
    path('user-profile/<int:pk>', views.user_profile_view, name='user_profile'),
]