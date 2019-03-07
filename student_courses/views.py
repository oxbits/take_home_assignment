from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import dateutil.parser
from .models import (
    Student,
    Teacher,
    Course,
)
from .serializers import (
    StudentSerializer,
    TeacherSerializer,
    CourseSerializer,
    WriteCourseSerializer,
)

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        print('self.action', self.action)
        if self.action in ('list', 'retrieve', ):
            return CourseSerializer
        if self.action in ('create', 'update', 'partial_update', 'destroy', ):
            return WriteCourseSerializer
        return CourseSerializer # serializers.Default # I dont' know what you want for create/destroy/update.                



@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def student_courses_search(request, format=None):

    if request.method == 'GET':

        if 'search_string' in request.query_params.keys():

            return(
                Response(
                    CourseSerializer(
                        context={'request': request}, 
                        instance=Course.objects.filter(
                            title__icontains=request.query_params['search_string']
                        ), 
                        many=True
                    ).data
                )
            )

    return(
        Response(
            "'search_string' get query parameter required"
        )
    )    


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def courses_date_search(request, format=None):

    if request.method == 'GET':

        if 'start_date' in request.query_params.keys() and 'operator' in request.query_params.keys():

            instance = None

            if request.query_params['operator'] == 'gt':

                instance = Course.objects.filter(
                    start_date__gt=dateutil.parser.parse(
                        request.query_params['start_date']
                    ).date()
                ) 
            
            elif request.query_params['operator'] == 'lt':
                    
                instance = Course.objects.filter(
                    start_date__lt=dateutil.parser.parse(
                        request.query_params['start_date']
                    ).date()
                )

            elif request.query_params['operator'] == 'gte':

                instance = Course.objects.filter(
                    start_date__gte=dateutil.parser.parse(
                        request.query_params['start_date']
                    ).date()
                )

            elif request.query_params['operator'] == 'lte':
 
                instance = Course.objects.filter(
                    start_date__lte=dateutil.parser.parse(
                        request.query_params['start_date']
                    ).date()
                )

            if instance:
                return(
                    Response(
                        CourseSerializer(
                            context={'request': request}, 
                            instance=instance, 
                            many=True
                        ).data
                    )
                )

    return(
        Response(
            "'date' and 'operator' get query parameter required"
        )
    )    
