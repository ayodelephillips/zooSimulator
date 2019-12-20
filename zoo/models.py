from django.db import models

class Monkey(models.Model):
    name=models.CharField(max_length=200)
    animalStatus = models.CharField(max_length=32, default='COMPLETELY HEALTHY')
    animalType = models.CharField(max_length=32, default='Monkey')
    healthPercentage = models.FloatField(default=100)



class Giraffe(models.Model):
    name=models.CharField(max_length=200)
    animalStatus = models.CharField(max_length=32, default='COMPLETELY HEALTHY')
    animalType = models.CharField(max_length=32, default='Giraffe')
    healthPercentage = models.FloatField(default=100)


class Elephant(models.Model):
    name=models.CharField(max_length=200)
    animalStatus = models.CharField(max_length=32, default='COMPLETELY HEALTHY')
    animalType = models.CharField(max_length=32, default='Elephant')
    healthPercentage = models.FloatField(default=100)

