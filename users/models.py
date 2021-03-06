from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from movies.models import Movies
from django.conf import settings
from django.db.models.signals import post_save


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_id = models.CharField(max_length=20, default=User.objects.all().count() + 1)
    age = models.CharField(max_length=20, default=' ')
    gender = models.CharField(max_length=20, default=' ')
    occupation = models.CharField(max_length=20, default=' ')


    def __str__(self):
        return self.user.username


class BucketList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_list = models.CharField(max_length=100000, default="")

    def __str__(self):
        return f'{self.user.username} BucketList'


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_list = models.CharField(max_length=100000, default="")

    def __str__(self):
        return f'{self.user.username}'


def post_save_watchlist_create(instance, created, *args, **kwargs):
    if created:
        WatchList.objects.get_or_create(user=instance)


post_save.connect(post_save_watchlist_create, sender=User)
