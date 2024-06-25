from django.contrib import admin
from .models import Course, Student, Enrollment, Instructor
# Register your models here.

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Student)
