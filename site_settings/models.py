from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(blank=True, null=True, help_text="URL")
    instagram = models.URLField(blank=True, null=True, help_text="URL")
    youtube = models.URLField(blank=True, null=True, help_text="URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("youtube"),
            FieldPanel("instagram"),

        ], heading="SocialMedia Settings")
    ]