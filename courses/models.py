from django.db import models

# Create your models here.
class Courses(models.Model):
	course_name = models.CharField(max_length=100)
	details = models.CharField(max_length=100)
	course_length = models.IntegerField()
	course_id = models.CharField(max_length=100)
	

    
	

