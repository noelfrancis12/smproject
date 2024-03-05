from django.db import models

# Create your models here.
# Create your models here.
class Userz(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    social_media_handles = models.CharField(max_length=100, blank=True, null=True)

class Post(models.Model):
    user = models.ForeignKey(Userz, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(Userz, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)