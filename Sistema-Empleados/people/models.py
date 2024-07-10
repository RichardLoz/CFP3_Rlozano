from django.db import models

class People(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    age = models.IntegerField()
    dni = models.CharField(max_length=8)
    position = models.ForeignKey(Position, null=True, on_delete =models.SET_NULL)


