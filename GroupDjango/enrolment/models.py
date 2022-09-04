from django.db import models


# Create your models here.
class Enrolment(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete= models.CASCADE)
    access = models.BooleanField(default=False)
    grade = models.PositiveSmallIntegerField(null=True)

class Result(models.Model):
    enrolment = models.ForeignKey(Enrolment, on_delete= models.CASCADE)
    question = models.ForeignKey('courses.Question', on_delete= models.CASCADE)
    result = models.BooleanField(null=True)
