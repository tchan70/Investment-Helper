from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name