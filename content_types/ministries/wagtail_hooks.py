from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import index


@hooks.register("register_admin_urls")
def register_calendar_url():
    return [
        path("ministries/", index, name="ministries"),
    ]


# @hooks.register("register_icons")
# def register_icons(icons):
#     return icons + ["hcn_website/ministires.svg"]


@hooks.register("register_admin_menu_item")
def register_frank_menu_item():
    return MenuItem(
        "Minstries", reverse("ministries"), icon_name="expand-right", order=10000
    )
