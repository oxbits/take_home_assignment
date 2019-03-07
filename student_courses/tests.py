from django.test import TestCase
import dateutil.parser
from .models import (
    Student,
    Teacher,
    Course,
)

# Create your tests here.

class StudentCoursesTestCase(TestCase):
    def setUp(self):
        
        student = Student.objects.create(
            name='test student',
        )

        teacher = Teacher.objects.create(
            name='test teacher',
        )

        course = Course.objects.create(
            title='test course',
            teacher=teacher,
            start_date='2019-01-01'
        )

        course.students.add(student)


    def test_student(self):
        student = Student.objects.get(name='test student')
        self.assertEqual(student.name, 'test student')
        

    def test_teacher(self):
        teacher = Teacher.objects.get(name='test teacher')
        self.assertEqual(teacher.name, 'test teacher')
        

    def test_course(self):
        course = Course.objects.get(title='test course')
        student = Student.objects.get(name='test student')
        teacher = Teacher.objects.get(name='test teacher')
        self.assertEqual(course.title, 'test course')
        self.assertEqual(course.teacher, teacher)
        self.assertEqual(course.students.all()[0], student)
        self.assertEqual(course.start_date, dateutil.parser.parse('2019-01-01').date())


    def test_student_courses_search(self):
        response = self.client.get('/student_courses_search/?search_string=test')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_student_courses_search_miss(self):
        response = self.client.get('/student_courses_search/?search_string=best')
        self.assertEqual(len(response.data), 0)


    def test_student_courses_search_no_search_string(self):
        response = self.client.get('/student_courses_search/?search_string=')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_student_courses_search_no_params(self):
        response = self.client.get('/student_courses_search/')
        self.assertEqual(response.data, "'search_string' get query parameter required")


    def test_courses_date_search_lt_hit(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-02&operator=lt')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_courses_date_search_lt_miss(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-01&operator=lt')
        self.assertEqual(len(response.data), 0)


    def test_courses_date_search_lte_hit(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-01&operator=lte')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_courses_date_search_lte_miss(self):
        response = self.client.get('/courses_date_search/?start_date=2018-12-31&operator=lte')
        self.assertEqual(len(response.data), 0)


    def test_courses_date_search_gt_hit(self):
        response = self.client.get('/courses_date_search/?start_date=2018-12-31&operator=gt')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_courses_date_search_gt_miss(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-01&operator=gt')
        self.assertEqual(len(response.data), 0)


    def test_courses_date_search_gte_hit(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-01&operator=gte')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            set(list(response.data[0].keys())), 
            {'url', 'title', 'id', 'start_date', 'teacher', 'students', }
        ) 
        self.assertEqual(response.data[0]['title'], 'test course')


    def test_courses_date_search_gte_miss(self):
        response = self.client.get('/courses_date_search/?start_date=2019-01-02&operator=gte')
        self.assertEqual(len(response.data), 0)


    def test_courses_date_search_no_params(self):
        response = self.client.get('/courses_date_search/')
        self.assertEqual(
            response.data, 
            "'date' and 'operator' get query parameter required"
        )


