import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import LocationRecord


# =========================================================
# LOCATION PAGE
# =========================================================

def location_page(request):

    return render(
        request,
        "tracker/location.html"
    )


# =========================================================
# SAVE LOCATION
# =========================================================

@csrf_exempt
@require_POST
def save_location(request):

    try:

        data = json.loads(request.body)

        # -------------------------------------------------
        # SESSION
        # -------------------------------------------------

        session_id = data.get(
            "session_id"
        )

        # -------------------------------------------------
        # LOCATION
        # -------------------------------------------------

        latitude = data.get(
            "latitude"
        )

        longitude = data.get(
            "longitude"
        )

        accuracy = data.get(
            "accuracy"
        )

        area = data.get(
            "area",
            ""
        )

        neighbourhood = data.get(
            "neighbourhood",
            ""
        )

        suburb = data.get(
            "suburb",
            ""
        )

        village = data.get(
            "village",
            ""
        )

        town = data.get(
            "town",
            ""
        )

        city = data.get(
            "city",
            ""
        )

        city_district = data.get(
            "city_district",
            ""
        )

        municipality = data.get(
            "municipality",
            ""
        )

        ward = data.get(
            "ward",
            ""
        )

        county = data.get(
            "county",
            ""
        )

        state = data.get(
            "state",
            ""
        )

        country = data.get(
            "country",
            ""
        )

        device_timestamp = data.get(
            "device_timestamp"
        )

        # -------------------------------------------------
        # DEVICE
        # -------------------------------------------------

        device_type = data.get(
            "device_type",
            ""
        )

        device_model = data.get(
            "device_model",
            ""
        )

        operating_system = data.get(
            "operating_system",
            ""
        )

        os_version = data.get(
            "os_version",
            ""
        )

        browser = data.get(
            "browser",
            ""
        )

        browser_version = data.get(
            "browser_version",
            ""
        )

        screen_width = data.get(
            "screen_width"
        )

        screen_height = data.get(
            "screen_height"
        )

        pixel_ratio = data.get(
            "pixel_ratio"
        )

        platform = data.get(
            "platform",
            ""
        )

        language = data.get(
            "language",
            ""
        )

        client_hint_platform = data.get(
            "client_hint_platform",
            ""
        )

        client_hint_platform_version = data.get(
            "client_hint_platform_version",
            ""
        )

        architecture = data.get(
            "architecture",
            ""
        )

        bitness = data.get(
            "bitness",
            ""
        )

        user_agent = data.get(
            "user_agent",
            ""
        )

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if not session_id:

            return JsonResponse(
                {
                    "success": False,
                    "error": "Session ID is required."
                },
                status=400
            )


        if (
            latitude is None
            or longitude is None
        ):

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
                    "error":
                        "Accuracy is required."
                },
                status=400
            )


        if not device_timestamp:

            return JsonResponse(
                {
                    "success": False,
                    "error":
                        "Timestamp is required."
                },
                status=400
            )


        # -------------------------------------------------
        # TIMESTAMP
        # -------------------------------------------------

        timestamp = datetime.fromisoformat(
            device_timestamp.replace(
                "Z",
                "+00:00"
            )
        )


        # -------------------------------------------------
        # CREATE RECORD
        # -------------------------------------------------

        location = LocationRecord.objects.create(

            session_id=session_id,

            latitude=latitude,

            longitude=longitude,

            accuracy=accuracy,

            area=area,

            neighbourhood=neighbourhood,

            suburb=suburb,

            village=village,

            town=town,

            city=city,

            city_district=city_district,

            municipality=municipality,

            ward=ward,

            county=county,

            state=state,

            country=country,

            device_timestamp=timestamp,

            device_type=device_type,

            device_model=device_model,

            operating_system=operating_system,

            os_version=os_version,

            browser=browser,

            browser_version=browser_version,

            screen_width=screen_width,

            screen_height=screen_height,

            pixel_ratio=pixel_ratio,

            platform=platform,

            language=language,

            client_hint_platform=
                client_hint_platform,

            client_hint_platform_version=
                client_hint_platform_version,

            architecture=architecture,

            bitness=bitness,

            user_agent=user_agent,

        )


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        return JsonResponse(
            {
                "success": True,

                "id":
                    location.id,

                "message":
                    "Location information saved successfully."
            }
        )


    except json.JSONDecodeError:

        return JsonResponse(
            {
                "success": False,
                "error":
                    "Invalid JSON data."
            },
            status=400
        )


    except Exception as error:

        return JsonResponse(
            {
                "success": False,
                "error":
                    str(error)
            },
            status=500
        )


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    search_query = request.GET.get(
        "q",
        ""
    ).strip()


    # -----------------------------------------------------
    # BASE QUERYSET
    # -----------------------------------------------------

    locations = LocationRecord.objects.order_by(
        "-device_timestamp",
        "-id"
    )


    # -----------------------------------------------------
    # GLOBAL SEARCH
    # -----------------------------------------------------

    if search_query:

        search_terms = search_query.split()


        for term in search_terms:

            locations = locations.filter(

                Q(country__icontains=term)
                |
                Q(county__icontains=term)
                |
                Q(neighbourhood__icontains=term)
                |
                Q(suburb__icontains=term)
                |
                Q(village__icontains=term)
                |
                Q(town__icontains=term)
                |
                Q(city__icontains=term)
                |
                Q(city_district__icontains=term)
                |
                Q(municipality__icontains=term)
                |
                Q(ward__icontains=term)
                |
                Q(state__icontains=term)
                |
                Q(area__icontains=term)
                |
                Q(device_type__icontains=term)
                |
                Q(device_model__icontains=term)
                |
                Q(operating_system__icontains=term)
                |
                Q(os_version__icontains=term)
                |
                Q(browser__icontains=term)
                |
                Q(browser_version__icontains=term)
                |
                Q(platform__icontains=term)
                |
                Q(language__icontains=term)
                |
                Q(client_hint_platform__icontains=term)
                |
                Q(client_hint_platform_version__icontains=term)
                |
                Q(architecture__icontains=term)
                |
                Q(bitness__icontains=term)
                |
                Q(user_agent__icontains=term)
                |
                Q(session_id__icontains=term)

            )


    # -----------------------------------------------------
    # CONTEXT
    # -----------------------------------------------------

    context = {

        "locations":
            locations,

        "total_locations":
            locations.count(),

        "search_query":
            search_query,

    }


    return render(
        request,
        "tracker/dashboard.html",
        context
    )


# =========================================================
# INDIVIDUAL RECORD
# =========================================================

@login_required
def location_detail(
    request,
    pk
):

    location = get_object_or_404(
        LocationRecord,
        pk=pk
    )


    return render(
        request,
        "tracker/location_detail.html",
        {
            "location":
                location
        }
    )


# =========================================================
# DELETE RECORD
# =========================================================

@login_required
@require_POST
def delete_location(
    request,
    pk
):

    location = get_object_or_404(
        LocationRecord,
        pk=pk
    )


    location.delete()


    return redirect(
        "tracker:dashboard"
    )