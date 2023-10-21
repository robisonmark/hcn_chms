from django.http import HttpResponse
from django.utils.html import format_html
from django.shortcuts import render
from wagtail.admin.ui.components import Component


class WelcomePanel(Component):
    def render_html(self, parent_context):
        return format_html(
            "<h1>{}</h1>",
            "Ministries are the ways in which we are seeking, serving, loving, becoming",
        )


def index(request):
    church_name = "HCN"
    return render(
        request,
        "index.html",
        {
            "church_name": church_name,
        },
    )
