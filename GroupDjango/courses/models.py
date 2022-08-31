from django.db import models
from django.forms import CharField

# Create your models here.

class Course(models.model):
    name = models.CharField(max_length=50)
    whatHeading = models.CharField(max_length=150)
    whatDescription = models.modelsTextField(max_length=500)
    howHeading = models.CharField(max_length=150)
    howDescription = models.modelsTextField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Topic(models.model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    intro = models.modelsTextField(max_length=500)

    def __str__(self):
        str = self.course + self.name
        return str

class Content(models.model):
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    explanation = models.modelsTextField(max_length=500)
    example = models.modelsTextField(max_length=500)

    def __str__(self):
        return self.name

class Questions(models.model):
    content = models.ForeignKey(Content, on_delete= models.CASCADE)
    question = models.CharField(max_length=50)
    answer = models.BooleanField()

    def __str__(self):
        str = self.id + self.name
        return str