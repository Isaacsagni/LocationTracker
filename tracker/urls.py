from django.urls import path
from . import views


app_name = "tracker"


urlpatterns = [

    # Location collection page
    path(
        "",
        views.location_page,
        name="location"
    ),

    # Save location API
    path(
        "api/save-location/",
        views.save_location,
        name="save_location"
    ),

    # Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # Individual location record
    path(
        "dashboard/location/<int:pk>/",
        views.location_detail,
        name="location_detail"
    ),

    # Delete individual location record
    path(
        "dashboard/location/<int:pk>/delete/",
        views.delete_location,
        name="delete_location"
    ),
]