from django.db import models
from django.contrib.auth.models import User


class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_groups = models.ManyToManyField(MuscleGroup)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.name
