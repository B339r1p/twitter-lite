from django.contrib import admin
from tweets.models import Tweet,Like,Retweet


# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Retweet)