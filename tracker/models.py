from django.db import models


class LocationRecord(models.Model):

    # =========================================================
    # SESSION
    # =========================================================

    session_id = models.CharField(
        max_length=100
    )

    # =========================================================
    # LOCATION
    # =========================================================

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    accuracy = models.FloatField()

    area = models.CharField(
        max_length=255,
        blank=True
    )

    neighbourhood = models.CharField(
        max_length=255,
        blank=True
    )

    suburb = models.CharField(
        max_length=255,
        blank=True
    )

    village = models.CharField(
        max_length=255,
        blank=True
    )

    town = models.CharField(
        max_length=255,
        blank=True
    )

    city = models.CharField(
        max_length=255,
        blank=True
    )

    city_district = models.CharField(
        max_length=255,
        blank=True
    )

    municipality = models.CharField(
        max_length=255,
        blank=True
    )

    ward = models.CharField(
        max_length=255,
        blank=True
    )

    county = models.CharField(
        max_length=255,
        blank=True
    )

    state = models.CharField(
        max_length=255,
        blank=True
    )

    country = models.CharField(
        max_length=255,
        blank=True
    )

    device_timestamp = models.DateTimeField()

    # =========================================================
    # DEVICE INFORMATION
    # =========================================================

    device_type = models.CharField(
        max_length=100,
        blank=True
    )

    device_model = models.CharField(
        max_length=255,
        blank=True
    )

    operating_system = models.CharField(
        max_length=100,
        blank=True
    )

    os_version = models.CharField(
        max_length=100,
        blank=True
    )

    browser = models.CharField(
        max_length=100,
        blank=True
    )

    browser_version = models.CharField(
        max_length=100,
        blank=True
    )

    screen_width = models.IntegerField(
        null=True,
        blank=True
    )

    screen_height = models.IntegerField(
        null=True,
        blank=True
    )

    pixel_ratio = models.FloatField(
        null=True,
        blank=True
    )

    platform = models.CharField(
        max_length=255,
        blank=True
    )

    language = models.CharField(
        max_length=100,
        blank=True
    )

    client_hint_platform = models.CharField(
        max_length=255,
        blank=True
    )

    client_hint_platform_version = models.CharField(
        max_length=255,
        blank=True
    )

    architecture = models.CharField(
        max_length=100,
        blank=True
    )

    bitness = models.CharField(
        max_length=50,
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    # =========================================================
    # DATA USAGE STATUS
    # =========================================================

    is_used = models.BooleanField(
        default=False
    )

    used_at = models.DateTimeField(
        null=True,
        blank=True
    )

    # =========================================================
    # SYSTEM TIMESTAMP
    # =========================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =========================================================
    # META
    # =========================================================

    class Meta:

        ordering = [
            "-created_at"
        ]

    # =========================================================
    # STRING REPRESENTATION
    # =========================================================

    def __str__(self):

        return (
            f"{self.area} - "
            f"{self.device_timestamp}"
        )