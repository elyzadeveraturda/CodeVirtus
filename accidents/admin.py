from django.contrib import admin
from .models import (
    AccidentReport,
    EdsaSegment,
    SeverityOption,
    WeatherOption,
    RoadConditionOption,
    TrafficVolumeOption,
)


@admin.register(AccidentReport)
class AccidentReportAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'date_time', 'severity', 'weather_condition', 'road_condition', 'traffic_volume', 'is_verified')
    list_filter = ('severity', 'weather_condition', 'road_condition', 'traffic_volume', 'is_verified', 'city')
    search_fields = ('location_name', 'description')


@admin.register(EdsaSegment)
class EdsaSegmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(SeverityOption)
class SeverityOptionAdmin(admin.ModelAdmin):
    list_display = ('code', 'label', 'order', 'is_active')
    list_editable = ('label', 'order', 'is_active')
    search_fields = ('code', 'label')


@admin.register(WeatherOption)
class WeatherOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


@admin.register(RoadConditionOption)
class RoadConditionOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


@admin.register(TrafficVolumeOption)
class TrafficVolumeOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)