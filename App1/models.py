from django.db import models

# Create your models here.
class BronzeSaint(models.Model):
    name = models.CharField(max_length=50)
    constellation = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class SilverSaint(models.Model):
    name = models.CharField(max_length=50)
    constellation = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class GoldSaint(models.Model):
    name = models.CharField(max_length=50)
    constellation = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name