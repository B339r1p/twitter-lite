from django.urls import path
from posts.views import homepage
urlpatterns = [
path('homepage/',homepage)
]
