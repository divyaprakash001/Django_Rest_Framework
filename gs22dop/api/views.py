# views.py
from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions
from .models import Student
from .serializer import StudentSerializer
from .permissions import IsStudentOwner

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsStudentOwner, DjangoObjectPermissions]

    def perform_create(self, serializer):
        # Assign teacher when creating a student
        teacher = self.request.user.teacher  # Assuming the user is a teacher
        serializer.save(teacher=teacher)
