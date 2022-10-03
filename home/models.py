from django.db import models

# Create your models here.

class Data(models.Model):

    end_year = models.CharField(max_length=50)
    intensity = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    insight = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    start_year = models.CharField(max_length=50)
    added = models.CharField(max_length=50)
    published = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    relevance = models.CharField(max_length=50)
    pestle = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    likelihood = models.CharField(max_length=50)
