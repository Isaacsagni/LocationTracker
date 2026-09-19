from django.db import models


class LocationRecord(models.Model):
    session_id = models.CharField(max_length=100)

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

    county = models.CharField(
        max_length=255,
        blank=True
    )

    country = models.CharField(
        max_length=255,
        blank=True
    )

    device_timestamp = models.DateTimeField()

    device_type = models.CharField(
        max_length=100,
        blank=True
    )

    operating_system = models.CharField(
        max_length=100,
        blank=True
    )

    browser = models.CharField(
        max_length=100,
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.area} - {self.device_timestamp}"