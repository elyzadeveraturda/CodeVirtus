from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages

from .models import (
    AccidentReport,
    EdsaSegment,
    SeverityOption,
    WeatherOption,
    RoadConditionOption,
    TrafficVolumeOption,
)
from .serializers import AccidentReportSerializer
from .permissions import AccidentRolePermission
from .forms import (
    SegmentFormSet,
    SeverityFormSet,
    WeatherFormSet,
    RoadConditionFormSet,
    TrafficVolumeFormSet,
)


def _is_data_entry_or_admin(user):
    """
    Encoder role (data entry):
    - Admins (is_staff) OR
    - Users in the 'Encoder' group.
    """
    return user.is_authenticated and (
        user.is_staff or user.groups.filter(name='Encoder').exists()
    )


def _is_enforcer_or_higher(user):
    """
    Officer role (enforcement):
    - Officers can view overview/predictions
    - Encoders and Admins are considered higher roles.
    """
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    return user.groups.filter(name__in=['Officer', 'Encoder']).exists()


class AccidentReportViewSet(viewsets.ModelViewSet):
    queryset = AccidentReport.objects.all().order_by('-date_time')
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated, AccidentRolePermission]


@login_required
@user_passes_test(_is_enforcer_or_higher)
def overview_dashboard(request):
    return render(request, 'overview.html')


@login_required
@user_passes_test(_is_data_entry_or_admin)
def data_entry(request):
    segments = EdsaSegment.objects.filter(is_active=True)
    severities = SeverityOption.objects.filter(is_active=True)
    weather_options = WeatherOption.objects.filter(is_active=True)
    road_options = RoadConditionOption.objects.filter(is_active=True)
    traffic_options = TrafficVolumeOption.objects.filter(is_active=True)

    context = {
        'segments': segments,
        'severities': severities,
        'weather_options': weather_options,
        'road_options': road_options,
        'traffic_options': traffic_options,
    }
    return render(request, 'entry.html', context)


@login_required
def maintenance_panel(request):
    """
    Unified maintenance panel for Admins to edit all dynamic reference data
    (segments, severities, weather, road conditions, traffic volume)
    in one screen that visually matches the data entry panel.
    """
    if not request.user.is_staff:
        # Only admins can access this panel
        return redirect('overview')

    if request.method == 'POST':
        segment_formset = SegmentFormSet(request.POST, prefix='segments')
        severity_formset = SeverityFormSet(request.POST, prefix='severities')
        weather_formset = WeatherFormSet(request.POST, prefix='weather')
        road_formset = RoadConditionFormSet(request.POST, prefix='road')
        traffic_formset = TrafficVolumeFormSet(request.POST, prefix='traffic')

        if (
            segment_formset.is_valid()
            and severity_formset.is_valid()
            and weather_formset.is_valid()
            and road_formset.is_valid()
            and traffic_formset.is_valid()
        ):
            segment_formset.save()
            severity_formset.save()
            weather_formset.save()
            road_formset.save()
            traffic_formset.save()
            messages.success(request, "Reference data updated successfully.")
            return redirect('maintenance')
        else:
            messages.error(request, "Please fix the errors below and try again.")
    else:
        segment_formset = SegmentFormSet(queryset=EdsaSegment.objects.all(), prefix='segments')
        severity_formset = SeverityFormSet(queryset=SeverityOption.objects.all(), prefix='severities')
        weather_formset = WeatherFormSet(queryset=WeatherOption.objects.all(), prefix='weather')
        road_formset = RoadConditionFormSet(queryset=RoadConditionOption.objects.all(), prefix='road')
        traffic_formset = TrafficVolumeFormSet(queryset=TrafficVolumeOption.objects.all(), prefix='traffic')

    context = {
        'segment_formset': segment_formset,
        'severity_formset': severity_formset,
        'weather_formset': weather_formset,
        'road_formset': road_formset,
        'traffic_formset': traffic_formset,
    }
    return render(request, 'maintenance.html', context)