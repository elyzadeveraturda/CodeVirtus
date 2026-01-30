from django.db import models
from django.utils import timezone

class AccidentReport(models.Model):
    # SEVERITY LEVELS
    SEVERITY_CHOICES = [
        ('MINOR', 'Minor (Property Damage)'),
        ('INJURY', 'Injury'),
        ('FATAL', 'Fatal'),
    ]

    # WHERE (Spatial)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_name = models.CharField(max_length=255, help_text="Specific street or landmark")
    city = models.CharField(max_length=50, default="Quezon City")

    # WHEN (Temporal)
    date_time = models.DateTimeField(default=timezone.now)

    # WHAT (Features for your ML Model)
    weather_condition = models.CharField(max_length=50, blank=True) # e.g. Rainy
    road_condition = models.CharField(max_length=50, blank=True)    # e.g. Wet
    traffic_volume = models.CharField(max_length=50, blank=True)    # e.g. High
    
    # DETAILS
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False) # For Admin approval
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location_name} - {self.severity}"