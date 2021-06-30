from tweets.serializers import TweetSerializer,LikeSerializer,RetweetSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Tweet,Like,Retweet



class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class LikeViewSet(viewsets.ModelViewSet):
    
    queryset = Like.objects.all()
    serializer_class = TweetSerializer



class RetweetViewSet(viewsets.ModelViewSet):
    
    queryset = Like.objects.all()
    serializer_class = RetweetSerializer