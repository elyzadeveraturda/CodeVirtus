from django.shortcuts import render
from rest_framework import viewsets
from .models import AccidentReport
from .serializers import AccidentReportSerializer

class AccidentReportViewSet(viewsets.ModelViewSet):
    # Get all reports, newest first
    queryset = AccidentReport.objects.all().order_by('-date_time')
    serializer_class = AccidentReportSerializer