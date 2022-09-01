from django.db import models
from django.forms import CharField

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    whatHeading = models.CharField(max_length=150)
    whatDescription = models.TextField(max_length=500)
    howHeading = models.CharField(max_length=150)
    howDescription = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    intro = models.TextField(max_length=500)

    def __str__(self):
        str = self.course.name + ", " + self.name
        return str

class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    explanation = models.TextField(max_length=500)
    example = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Questions(models.Model):
    content = models.ForeignKey(Content, on_delete= models.CASCADE)
    question = models.CharField(max_length=50)
    answer = models.BooleanField()

    def __str__(self):
        return self.question