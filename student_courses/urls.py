from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from student_courses import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'course', views.CourseViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'teacher', views.TeacherViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^student_courses_search/$', views.student_courses_search),
    url(r'^courses_date_search/$', views.courses_date_search),
]

