from django.db import models

# Create your models here.

class paperModel(models.Model):
    paper = models.FileField(upload_to = 'questionpaper')
    course_code = models.CharField(max_length = 5)
    year = models.IntegerField()
    tierce = models.IntegerField()
    instructor = models.CharField(max_length = 30, blank = True)

class courseModel(models.Model):
    program = models.CharField(max_length = 5)
    course_type = models.CharField(max_length = 20)
    department = models.CharField(max_length = 4, blank = True)
    course_name = models.CharField(max_length = 30)
    course_code = models.CharField(max_length = 5)
