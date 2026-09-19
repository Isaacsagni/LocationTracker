import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import LocationRecord


def location_page(request):
    return render(
        request,
        "tracker/location.html"
    )


@csrf_exempt
@require_POST
def save_location(request):

    try:

        data = json.loads(request.body)

        session_id = data.get("session_id")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        accuracy = data.get("accuracy")

        area = data.get(
            "area",
            ""
        )

        county = data.get(
            "county",
            ""
        )

        country = data.get(
            "country",
            ""
        )

        device_timestamp = data.get(
            "device_timestamp"
        )


        if not session_id:

            return JsonResponse(
                {
                    "success": False,
                    "error": "Session ID is required."
                },
                status=400
            )


        if latitude is None or longitude is None:

            return JsonResponse(
                {
                    "success": False,
                    "error":
                        "Latitude and longitude are required."
                },
                status=400
            )


        if accuracy is None:

            return JsonResponse(
                {
                    "success": False,
                    "error": "Accuracy is required."
                },
                status=400
            )


        if not device_timestamp:

            return JsonResponse(
                {
                    "success": False,
                    "error": "Timestamp is required."
                },
                status=400
            )


        timestamp = datetime.fromisoformat(

            device_timestamp.replace(
                "Z",
                "+00:00"
            )

        )


        location = LocationRecord.objects.create(

            session_id=session_id,

            latitude=latitude,

            longitude=longitude,

            accuracy=accuracy,

            area=area,

            county=county,

            country=country,

            device_timestamp=timestamp,

        )


        return JsonResponse(
            {
                "success": True,

                "id": location.id,

                "message":
                    "Location saved successfully."
            }
        )


    except json.JSONDecodeError:

        return JsonResponse(
            {
                "success": False,
                "error": "Invalid JSON data."
            },
            status=400
        )


    except Exception as error:

        return JsonResponse(
            {
                "success": False,
                "error": str(error)
            },
            status=500
        )


@login_required
def dashboard(request):

    locations = LocationRecord.objects.order_by(
        "-device_timestamp",
        "-id"
    )


    latest_location = locations.first()


    context = {

        "locations": locations,

        "latest_location":
            latest_location,

        "total_locations":
            locations.count(),

    }


    return render(

        request,

        "tracker/dashboard.html",

        context

    )