from django.db import models

# Create your models here.
class Enrolment(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete= models.CASCADE)
    access = models.BooleanField(default=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        str = self.user.username + "-" + self.course.name
        return str

class Result(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE)
    question = models.ForeignKey('courses.Question', on_delete= models.CASCADE)
    result = models.BooleanField(null=True)
