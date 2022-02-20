from django.db import models


# Create your models here.



class djangoClasses(models.Model):
    title = models.CharField(max_length=100)
    courseNumber = models.IntegerField(blank=True, null=True)
    instructorName = models.CharField(max_length=100)
    duration = models.FloatField(null=True, blank=True, default=None)

    objects = models.Manager()




def __str__(self):
    return f"(self.title), (self.courseNumber), (instructorName), (duration)"