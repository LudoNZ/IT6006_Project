from unittest import result
from django.db import models

# Create your models here.
class Enrolment(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete= models.CASCADE)
    access = models.BooleanField(default=True)
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        str = self.user.username + "-" + self.course.name
        return str

class Result(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE)
    question = models.ForeignKey('courses.Question', on_delete= models.CASCADE)
    result = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.question} - {self.user} - {self.result}'