from django.urls import path
from . import views

urlpatterns = [
    path('room-detail/<int:pk>', views.room_detail_view, name='room_detail'),
    path('create-room/', views.create_room_view, name='create_room'),
    path('update-room/<int:pk>', views.update_room_view, name='update_room'),
    path('delete-room/<int:pk>', views.delete_room_view, name='delete_room'),
]