from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, unique=True, default="No title")
    cover_image = models.ImageField(upload_to="covers/")
    description = models.TextField(max_length=256, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)

    def __str__(self):
        return self.title


class WebSeries(models.Model):
    title = models.CharField(max_length=50, unique=True, default="No title")
    cover_image = models.ImageField(upload_to="covers/")
    description = models.TextField(max_length=256, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
