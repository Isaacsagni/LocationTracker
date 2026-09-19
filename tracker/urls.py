from django.urls import path

from . import views


app_name = "tracker"


urlpatterns = [

    path(
        "",
        views.location_page,
        name="location"
    ),

    path(
        "api/save-location/",
        views.save_location,
        name="save_location"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

]