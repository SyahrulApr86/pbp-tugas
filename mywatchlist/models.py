from django.db import models

# Create your models here.
class ItemWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()

    def __str__(self):
        return self.title