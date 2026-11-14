from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    price = models.FloatField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title