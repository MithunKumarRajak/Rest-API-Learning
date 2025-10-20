from django.db import models

# Create your models here.


class Student(models.Model):
    Student_id = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    branch = models.TextField(max_length=100)

    def __str__(self):
        return self.name
