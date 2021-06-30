from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from tweets.views import TweetViewSet, LikeViewSet,RetweetViewSet

router = routers.DefaultRouter()
router.register(r'', TweetViewSet)
router.register(r'like', LikeViewSet)
router.register(r'retweet', RetweetViewSet)

urlpatterns = [
    path("", include(router.urls))
]