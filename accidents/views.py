from django.shortcuts import render
from rest_framework import viewsets
from .models import AccidentReport
from .serializers import AccidentReportSerializer
from .permissions import IsAdminOrNoDelete
from rest_framework.permissions import IsAuthenticated

class AccidentReportViewSet(viewsets.ModelViewSet):
    # Get all reports, newest first
    queryset = AccidentReport.objects.all().order_by('-date_time')
    serializer_class = AccidentReportSerializer
    # This enforces the rules:
    # 1. User MUST be logged in (IsAuthenticated)
    # 2. User MUST pass our custom check (IsAdminOrNoDelete)
    permission_classes = [IsAuthenticated, IsAdminOrNoDelete]