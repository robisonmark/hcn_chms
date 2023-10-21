from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import index


@hooks.register("register_admin_urls")
def register_calendar_url():
    return [
        path("staff/", index, name="staff"),
    ]


# @hooks.register("register_icons")
# def register_icons(icons):
#     return icons + ["hcn_website/ministires.svg"]


@hooks.register("register_admin_menu_item")
def register_frank_menu_item():
    return MenuItem("Staff", reverse("staff"), icon_name="group", order=10000)
