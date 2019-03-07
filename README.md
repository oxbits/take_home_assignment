# Take‐Home Assignment

----

#### Versions: 

- Python 3.7.2
- PostgreSQL 9.6.11
- djangorestframework 3.9.2
- docker-compose version 1.23.2, build 1110ad01

---

Based on the requirements we understand there are these objects:

- student
- teacher
- course

---

#### API Root:

http://0.0.0.0:8000/

#### List Endpoints:

http://0.0.0.0:8000/student/

http://0.0.0.0:8000/teacher/

http://0.0.0.0:8000/course/

#### Notes on Requirements:

- Course list and detail contains an embedded list of enrolled students.

- Student list and detail contains an embedded list of courses.

- All CRUD functions for all objects are supported in API.

- Django rest framework HTML API provides browser access to HTTP methods.

- All json objects have hyperlinks to detail endpoints.

----

http://0.0.0.0:8000/student_courses_search/?search_string=basket

- Search by substring in title returns list of matching courses with embedded teacher and students objects


----

http://0.0.0.0:8000/courses_date_search/?start_date=2019-01-01&operator=lte

- Search by start date takes an ISO date and 
  - lt - less than
  - gt - greater than
  - lte - less than equal
  - gte - greater than equal

----

#### Admin:

http://0.0.0.0:8000/admin/

----

- Throttling is implemented: 720 requests per hour

- The requirements were clear enough to interpret this implementation.

- Time estimate of 1.5 hours per each: understanding, designing, coding, testing

- I started the project working on an auth model, but quickly decided not to implement auth do to time contraints.  If I had more time I would implement auth.

- With more time I would work on scaling the app better for huge numbers of students, teachers, and course.  The current admin UI (drop downs, etc.) would not handle large numbers well.

- I am pleased with the use of inherited/extended course serializers along with **get_serializer_class** in the **CourseViewSet**.  Simply changing the **depth** value between 0 and 1 in the **Meta class** of the serializers allows for either simplified display of embedded objects, or simplified writes via the form at the bottom of the djangorestframework API HTML pages.
