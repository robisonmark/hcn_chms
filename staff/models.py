from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.panels import PageChooserPanel
from wagtail.fields import RichTextField, StreamField

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
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ministry_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )   
    
    staff_bio = RichTextField()
    fun_facts = RichTextField()
    ministry_links = StreamField(
        [
            ("ministries", blocks.MinistryLinksBlock())
            # PageChooserPanel('ministry_page')
        ],
        use_json_field=False,
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('given_name'),
        FieldPanel('family_name'),
        FieldPanel('position'),
        FieldPanel('staff_bio'),
        FieldPanel('fun_facts'),
        FieldPanel('ministry_links'),
        FieldPanel('image'),
    ]

    api_fields = [
        APIField("given_name"),
    #     APIField("sectionHeader"),
    #     APIField("content"),
    #     APIField("subsections"),
    ]


# class StaffPageMinistryLink(Orderable):
#     page = ParentalKey(StaffPage, on_delete=models.CASCADE, related_name='ministry_links')
#     name