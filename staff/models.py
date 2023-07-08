from django.db import models

from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import PageChooserPanel, FieldPanel
from wagtail.fields import RichTextField, StreamField
from rest_framework import serializers

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
    email = models.CharField(null=False, blank=False, max_length=100, default='')
    
    COMPONENT_CHOICES =  [('CircleImageStacked', 'CircleImageStacked')]
    component = models.CharField(
        max_length=50,
        choices=COMPONENT_CHOICES,
        default = 'CircleImageStacked'
    )


    content_panels = Page.content_panels + [
        FieldPanel('given_name'),
        FieldPanel('family_name'),
        FieldPanel('email'),
        FieldPanel('position'),
        FieldPanel('staff_bio'),
        FieldPanel('fun_facts'),
        FieldPanel('ministry_links'),
        FieldPanel('image'),
    ]

    api_fields = [
        APIField("given_name"),
        APIField('family_name'),
        APIField('email'),
        APIField('position'),
        APIField('staff_bio'),
        APIField('fun_facts'),
        APIField('ministry_links'),
        APIField('image'),
        APIField('component'),
        APIField('email'),
        APIField('full_name', serializer=serializers.StringRelatedField()),
        APIField('container', serializer=serializers.StringRelatedField()),
        APIField('tileButton', serializer=serializers.DictField()),
        APIField('tileContent', serializer=serializers.DictField()),
    ]

    @property
    def container(self):
        return 'Staff'
    
    @property
    def tileButton(self):
        return {
            'url': f'mailto: {self.email}',
            'cta': f'Contact {self.position} {self.given_name}'
        }

    @property
    def tileContent(self):
        return {
            'headline': f'{self.given_name} {self.family_name}',
            'description': self.position
        }

# class StaffPageMinistryLink(Orderable):
#     page = ParentalKey(StaffPage, on_delete=models.CASCADE, related_name='ministry_links')
#     name