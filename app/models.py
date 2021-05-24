from django.db import models


# Create your models here.

class Store(models.Model):
    name = models.CharField('Title', max_length=150)
    address = models.CharField('Address', max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Title', max_length=2)
    detail = models.TextField('Detail', max_length=250, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    poster = models.ImageField('Image', blank=True, null=True)

    def __str__(self):
        return self.name
