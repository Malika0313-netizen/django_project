from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title




class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    model = models.CharField(max_length=50000)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    course = models.IntegerField()

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.CharField(max_length=10000)

    def __str__(self):
        return self.title



class Car2(models.Model):
    brend = models.CharField(max_length=100)
    model = models.CharField(max_length=500)
    year = models.CharField(max_length=5000)

    def __str__(self):
        return self.brend



class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100000)
    description = models.TextField()

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name