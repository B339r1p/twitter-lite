from .models import Tweet,Like,Retweet
from rest_framework.serializers import ModelSerializer

class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class RetweetSerializer(ModelSerializer):
    class Meta:
        model = Retweet
        fields = "__all__"
