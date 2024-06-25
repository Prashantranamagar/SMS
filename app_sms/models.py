from django.db import models


class Student(models.Model):
    """
    Represents a student in the school database.
    """

    first_name = models.CharField(
        max_length=30,
        help_text="The first name of the student. "
                  "Maximum length is 30 characters."
    )
    last_name = models.CharField(
        max_length=30,
        help_text="The last name of the student. "
                  "Maximum length is 30 characters."
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        help_text="The email address of the student. Must be unique."
    )
    date_of_birth = models.DateField(
        help_text="The date of birth of the student."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "student"
        verbose_name_plural = "students"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, blank=True, null=True)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2,
                                     blank=True, null=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='instructors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
