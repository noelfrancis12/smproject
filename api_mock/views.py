from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from .models import Userz, Post, Comment
# Create your views here.
def get_timeline(request, user_id):
    posts = Post.objects.filter(user_id=user_id)
    data = [{'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]
    return JsonResponse(data, safe=False)

def get_user_profile(request, user_id):
    user = Userz.objects.get(pk=user_id)
    data = {'username': user.username, 'bio': user.bio, 'social_media_handles': user.social_media_handles}
    return JsonResponse(data)

def get_notifications(request, user_id):
    # Implement your notification logic here
    notifications = [{'message': 'You have a new comment!'}, {'message': 'Your post got a like!'}]
    return JsonResponse(notifications, safe=False)