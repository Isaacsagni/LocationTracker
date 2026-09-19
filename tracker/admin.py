from django.contrib import admin

from .models import LocationRecord


@admin.register(LocationRecord)
class LocationRecordAdmin(admin.ModelAdmin):

    list_display = (
        "area",
        "county",
        "country",
        "latitude",
        "longitude",
        "accuracy",
        "device_timestamp",
        "created_at",
    )

    list_filter = (
        "country",
        "county",
    )

    search_fields = (
        "area",
        "county",
        "country",
        "session_id",
    )

    ordering = (
        "-created_at",
    )