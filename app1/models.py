from django.db import models


# Create your models here.

class Persons(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phno = models.IntegerField()


    def __str__(self):
        return self.name