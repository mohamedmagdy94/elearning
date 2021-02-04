from djongo import models

# Create your models here.

class Course(models.Model):
    _id = models.ObjectIdField()
    identifier = models.IntegerField()
    course_title = models.CharField(max_length=200)
    num_subscribers = models.IntegerField()
    subject = models.CharField(max_length=200)

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.IntegerField()
    courses = models.ArrayField(model_container=Course)


class Lecture(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    attachment = models.CharField(max_length=200)
    courses = models.ArrayField(model_container=Course)


