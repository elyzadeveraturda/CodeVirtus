from django.contrib import admin
from .models import AccidentReport

# This makes the table visible in the Admin Panel
@admin.register(AccidentReport)
class AccidentReportAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'date_time', 'severity', 'is_verified')
    list_filter = ('severity', 'is_verified', 'city')
    search_fields = ('location_name', 'description')