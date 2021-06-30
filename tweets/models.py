from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    content = models.TextField()
    text = models.CharField(max_length = 60 )
    created_on = models.DateTimeField(auto_now_add = True)
    updated_created_on = models.DateTimeField(auto_now = True)
    user_like = models.ForeignKey(User, on_delete =models.CASCADE)




class Like(models.Model):
    user_like = models.ForeignKey(User, on_delete =models.CASCADE)
    user_tweet = models.ForeignKey(Tweet, on_delete =models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)



class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)