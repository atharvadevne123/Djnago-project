from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department, Attendance, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, AttendanceSerializer, PerformanceSerializer
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['department', 'date_of_joining']
    ordering_fields = ['name', 'date_of_joining']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'date', 'status']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'rating', 'review_date']
