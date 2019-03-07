from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(
        max_length=256, blank=True, null=True, default='', 
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):

    name = models.CharField(
        max_length=256, blank=True, null=True, default='', 
    )

    def __str__(self):
        return self.name


class Course(models.Model):

    title = models.CharField(
        max_length=256, blank=True, null=True, default='', 
    )

    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True, 
        related_name='teacher_courses'
        )

    students = models.ManyToManyField(
        Student, blank=True, related_name='student_courses'
        )

    start_date = models.DateField(blank=True, null=True, )

    def __str__(self):
        return self.title