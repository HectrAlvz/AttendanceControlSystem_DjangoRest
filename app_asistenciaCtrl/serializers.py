from rest_framework import serializers
from .models import CompanyModels, WorkerModels, AttendanceModels

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModels
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerModels
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModels
        fields = '__all__'