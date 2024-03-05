# mock_api/urls.py
from django.urls import path
from .views import get_timeline, get_user_profile, get_notifications

urlpatterns = [
    path('timeline/<int:user_id>/', get_timeline, name='timeline'),
    path('profile/<int:user_id>/', get_user_profile, name='user_profile'),
    path('notifications/<int:user_id>/', get_notifications, name='notifications'),
]