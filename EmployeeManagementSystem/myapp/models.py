from django.db import models

class Employee(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.fname