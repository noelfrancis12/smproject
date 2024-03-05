from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Details(models.Model):
    userc=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    image=models.ImageField(upload_to="image/",null=True) 
