from rest_framework import serializers
from .models import (
    Student,
    Teacher,
    Course,
)


class WriteCourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = (
            'url',
            'id',
            'title',
            'teacher',
            'students',
            'start_date',
        )


class CourseSerializer(WriteCourseSerializer):

    class Meta(WriteCourseSerializer.Meta):
        depth = 1


class StudentCourseSerializer(CourseSerializer):

    class Meta(CourseSerializer.Meta):
        fields = (
            'url',
            'id',
            'title',
            'teacher',
            'start_date',
        )


class TeacherCourseSerializer(CourseSerializer):

    class Meta(CourseSerializer.Meta):
        fields = (
            'url',
            'id',
            'title',
            'students',
            'start_date',
        )


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    student_courses = StudentCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = (
            'url',
            'id',
            'name',
            'student_courses',
        )


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    teacher_courses = TeacherCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = (
            'url',
            'id',
            'name',
            'teacher_courses',
        )

