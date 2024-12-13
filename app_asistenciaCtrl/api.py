from .models import CompanyModels, WorkerModels, AttendanceModels
from rest_framework import viewsets, permissions
from .serializers import CompanySerializer, WorkerSerializer, AttendanceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModels.objects.all()
    permission_classes = [permissions.AllowAny] #.IsAuthenticated
    serializer_class = CompanySerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = WorkerModels.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WorkerSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = AttendanceModels.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AttendanceSerializer
