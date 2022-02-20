from django.contrib import admin

# Register your models here.
from .models import Course Number, Duration, Instructor Name, Title

admin.site.register(Title)
admin.site.register(Course Number)
admin.site.register(Instructor Name)
admin.site.register(Duration)