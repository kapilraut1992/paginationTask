from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    marks=models.FloatField()

    def __str__(self):
        return self.fname