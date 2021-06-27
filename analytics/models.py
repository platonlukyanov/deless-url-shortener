from django.db import models


class LinkOpening(models.Model):
    link = models.ForeignKey('shortener.Link', on_delete=models.CASCADE, related_name="openings")

    # Not required Statistic Information
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    from_site = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=8, null=True, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=6, null=True, blank=True)
    time_for_opener = models.DateTimeField(null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    browser = models.CharField(max_length=50, null=True, blank=True)
    os = models.CharField(max_length=50, null=True, blank=True)\


    created = models.DateTimeField(auto_now_add=True, db_index=True)





