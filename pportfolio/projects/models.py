from django.db import models

# Create your models here.

class Project_inv(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='static\images')
    #image2 = models.FileField()

class Project_inv2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField()

class Project_inv3(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    detailed_description = models.TextField()
    technology = models.CharField(max_length=200)
    github = models.URLField(blank=True)
    image = models.FileField()

# class Project_inv4(models.Model):
#     title = models.CharField(max_length=100)
#     short_description = models.CharField(max_length=300)
#     detailed_description = models.TextField()
#     technology = models.CharField(max_length=200)
#     github = models.URLField(blank=True)
#     image = models.FilePathField(path='static\images')