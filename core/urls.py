from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('topics/', views.topics_page_view, name='topics'),
    path('activity/', views.activity_paga_view, name='activity'),
]