from django.db import models

# Create your models here.

class Sponsors(models.Model):
    sponsor_name = models.TextField()
    sponsor_image = models.TextField()
    sponsor_id = models.IntegerField(primary_key=True)
    sponsor_description = models.TextField()

    def __str__(self):
        return self.sponsor_name
    