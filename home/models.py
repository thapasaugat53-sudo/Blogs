from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to = 'static/photo', null=True, blank=True)
    def __str__(self):
        return f"{self.title}"
    
