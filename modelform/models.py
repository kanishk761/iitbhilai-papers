from django.db import models

# Create your models here.

class userDetails(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField()
