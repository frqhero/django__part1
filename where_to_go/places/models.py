from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title
