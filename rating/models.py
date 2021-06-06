from django.db import models
from django.contrib.auth.models import User
from movies.models import Movies


class Rating(models.Model):
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.FloatField()


    def __str__(self):
        return str(self.rating)
