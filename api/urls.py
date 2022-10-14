from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_rountes_view),
    path('rooms/', views.get_rooms_views),
    path('rooms/<int:pk>', views.get_room_detail_views),
]
