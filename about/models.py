from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail_headless_preview.models import HeadlessPreviewMixin

from streams import blocks


class StreamFieldsPage(HeadlessPreviewMixin, Page):
    document = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [InlinePanel("section")]

    api_fields = [APIField("section")]


class PageContent(Orderable):
    page = ParentalKey(
        StreamFieldsPage, on_delete=models.CASCADE, related_name="section"
    )
    displaySectionTitle = models.BooleanField(default=True)
    sectionHeader = models.CharField(null=True, blank=True, max_length=150)
    content = RichTextField(null=True, blank=True)

    subsections = StreamField(
        [
            ("paragraph", blocks.ParagraphRichTextBlock()),
            # ("table_block", blocks.TableBlock())
            ("logo_block", blocks.LogoBlock()),
            ('document_block', blocks.DocumentBlock())
            

        ],
        null=True,
        blank=True,
    )
    panels = [
        FieldPanel("sectionHeader"),
        FieldPanel("displaySectionTitle"),
        FieldPanel("content"),
        StreamFieldPanel("subsections"),
    ]

    api_fields = [
        APIField("displaySectionTitle"),
        APIField("sectionHeader"),
        APIField("content"),
        APIField("subsections"),
    ]
