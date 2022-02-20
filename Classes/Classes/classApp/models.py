from django.db import models
from models

# Create your models here.
class djangoManager(models.Manager):
    def create_title(self, title):
        title = self.create(title=title)
        return title
    def create_courseNumber(self, coursNumber):
        course = self.create(courseNumber=courseNumber)
        return course
    def create_instructorName(self, instructorName):
        instructor = self.create(instructorName=instructorName)
        return instructor
    def create_duration(self, duration):
        duration = self.create(duration=duration)
        return duration



class djangoClasses(models.Model):
    title = models.Charfield(max_length=100)
    courseNumber = models.IntegerField
    instructorName = models.Charfield(max_length=100)
    duration = models.Floatfield

    objects = models.Manager()

title = djangoClasses.objects.create_title("software developer")
course = djangoClasses.objects.create_courseNumber("343")
instructor = djangoClasses.objects.create_instructorName("Eric")
duration = djangoClasses.objects.create_duration("eternity minus a week")


def __str__(self):
    return self.name
