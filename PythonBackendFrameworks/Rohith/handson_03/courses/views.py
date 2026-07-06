from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    This single class handles all 5 standard database actions automatically:
    - GET /api/courses/      -> Lists all courses
    - POST /api/courses/     -> Creates a new course
    - GET /api/courses/id/   -> Grabs one single course details
    - PUT /api/courses/id/   -> Updates an existing course
    - DELETE /api/courses/id/-> Removes a course permanently
    """
    # Tell Django where to look in the database to get the courses
    queryset = Course.objects.all()
    
    # Tell Django which serializer blueprint to use to convert database rows to JSON
    serializer_class = CourseSerializer

    # This creates a special, custom endpoint: GET /api/courses/{id}/students/
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        # 1. Grab the specific course requested using the ID from the URL path
        course = self.get_object()
        
        # 2. Go to the Student table, look through the student's enrollments, 
        #    and find only the students who are enrolled in this specific course.
        enrolled_students = Student.objects.filter(enrollments__course=course)
        
        # 3. Translate that database list of filtered students into clean JSON text
        serializer = StudentSerializer(enrolled_students, many=True)
        
        # 4. Send the student data back to the user with a successful 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentViewSet(viewsets.ModelViewSet):
    """
    Handles all student data actions (List, Create, Update, Delete) automatically.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    Handles all student enrollment rows (List, Create, Update, Delete) automatically.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer