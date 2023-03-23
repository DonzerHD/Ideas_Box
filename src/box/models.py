from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Ideas_Box(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.PositiveIntegerField(default=0)
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Ideas_Box, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'box')