from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    companyName = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class News(models.Model):
    symbol = models.CharField(max_length=10)
    title = models.CharField(max_length=1000)
    snippet = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Risk(models.Model):
    risk = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Savings(models.Model):
    risk = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name