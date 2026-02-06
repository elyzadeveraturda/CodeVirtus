from django.forms import modelformset_factory

from .models import (
    EdsaSegment,
    SeverityOption,
    WeatherOption,
    RoadConditionOption,
    TrafficVolumeOption,
)


SegmentFormSet = modelformset_factory(
    EdsaSegment,
    fields=("name", "is_active"),
    extra=1,
    can_delete=True,
)

SeverityFormSet = modelformset_factory(
    SeverityOption,
    fields=("code", "label", "order", "is_active"),
    extra=1,
    can_delete=True,
)

WeatherFormSet = modelformset_factory(
    WeatherOption,
    fields=("name", "order", "is_active"),
    extra=1,
    can_delete=True,
)

RoadConditionFormSet = modelformset_factory(
    RoadConditionOption,
    fields=("name", "order", "is_active"),
    extra=1,
    can_delete=True,
)

TrafficVolumeFormSet = modelformset_factory(
    TrafficVolumeOption,
    fields=("name", "order", "is_active"),
    extra=1,
    can_delete=True,
)

