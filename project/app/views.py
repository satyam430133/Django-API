from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class StudentList(viewsets.ModelViewSet):
    serializer_class = StulistSerializer
    queryset = StuModel.objects.all()