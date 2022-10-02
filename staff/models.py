from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class StaffPage(Page):
    given_name = models.CharField(
        null=False, blank=False, max_length=100, default="Given Name"
    )
    family_name = models.CharField(
        null=False, blank=False, max_length=100, default="Family Name"
    )
    position = models.CharField(
        null=False, blank=False, max_length=100, default="Pastor"
    )
    staff_bio = blocks.StaffBioBlock()
    # image = models.ForeignKey(
    #     'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    # )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )   
    

    # staff_bio = StreamField(
    #     [
    #         ("staff_bio", blocks.StaffBioBlock()),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    content_panels = Page.content_panels + [
        FieldPanel('given_name'),
        FieldPanel('family_name'),
        FieldPanel('position'),
        # StreamFieldPanel('staff_bio'),
        ImageChooserPanel('image'),
    ]

    api_fields = [
        APIField("given_name"),
    #     APIField("sectionHeader"),
    #     APIField("content"),
    #     APIField("subsections"),
    ]
