from django.contrib import admin
from .models import WebSeries
from .models import Movie

# Register your models here.
admin.site.register(WebSeries)
admin.site.register(Movie)
