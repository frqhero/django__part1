from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    long_description = HTMLField(blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    class Meta:
        ordering = ['order']

    order = models.IntegerField(default=0)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()

    def __str__(self):
        return f'{self.order} {self.place.title}'
