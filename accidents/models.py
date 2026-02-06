from django.db import models
from django.utils import timezone


class EdsaSegment(models.Model):
    """
    Configurable list of EDSA segments used in the Admin Data Entry form.
    Admin users can maintain this list in the Django admin instead of
    editing the code.
    """
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SeverityOption(models.Model):
    """
    Dynamic list of severity levels (e.g., Minor, Injury, Fatal).
    Admins manage these options via the maintenance module.
    """
    code = models.CharField(max_length=20, unique=True, help_text="Machine-friendly code, e.g. MINOR")
    label = models.CharField(max_length=50, help_text="Human label, e.g. Minor")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'label']

    def __str__(self):
        return self.label


class WeatherOption(models.Model):
    """
    Dynamic list of weather conditions (e.g., Clear, Rainy).
    """
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class RoadConditionOption(models.Model):
    """
    Dynamic list of road conditions (e.g., Dry, Wet).
    """
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class TrafficVolumeOption(models.Model):
    """
    Dynamic list of traffic volume levels (e.g., Low, Medium, High).
    """
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class AccidentReport(models.Model):
    # WHERE (Spatial)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_name = models.CharField(max_length=255, help_text="Specific street or landmark")
    city = models.CharField(max_length=50, default="Quezon City")

    # WHEN (Temporal)
    date_time = models.DateTimeField(default=timezone.now)

    # WHAT (Features for your ML Model)
    weather_condition = models.CharField(max_length=50, blank=True)  # e.g. Rainy
    road_condition = models.CharField(max_length=50, blank=True)     # e.g. Wet
    traffic_volume = models.CharField(max_length=50, blank=True)     # e.g. High

    # DETAILS
    severity = models.CharField(max_length=20)  # free text, but UI is driven by SeverityOption
    description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # For Admin approval
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location_name} - {self.severity}"