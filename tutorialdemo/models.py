from django.db import models

# Create your models here.

class product(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to="documents/")
    def __str__(self):
        return self.name