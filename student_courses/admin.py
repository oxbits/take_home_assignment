from django.contrib import admin
from .models import (
    Student,
    Teacher,
    Course,
)

class StudentInline(admin.TabularInline):
    model = Course.students.through
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
    exclude = ['students']

class StudentCourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        StudentCourseInline,
    ]

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1
    exclude = ['students']


class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline,
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
