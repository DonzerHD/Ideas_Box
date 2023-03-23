from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Ideas_Box(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Ideas_Box, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')], default='upvote')
    class Meta:
        unique_together = ('user', 'box')