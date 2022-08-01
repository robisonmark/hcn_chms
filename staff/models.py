from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page


class StaffPage(Page):
    given_name = models.CharField(
        null=False, blank=False, max_length=100, default="Name"
    )
    family_name = models.CharField(
        null=False, blank=False, max_length=100, default="Name"
    )
    position = models.CharField(
        null=False, blank=False, max_length=100, default="Pastor"
    )
