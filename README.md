# Church Management Systen

## Hendersonville Church of the Nazarene

This is the foundational build for a new church management software platform working to address the rigid templates used by most ChMS. This build is for Hendersonville Church of the Nazarene

## Libraries

1. Virtualenv
2. Wagtail

## Installation - First Time

1. Clone Repo
2. Navigate to newly created folder
3. In Powershell run:
4. `python -m venv chms`
5. `.\chms\Scripts\activate`
6. `pip install -r requirements.txt`
7. `python manage.py migrate`
8. `python manage.py createsuperuser` and follow prompts
9. `python manage.py runserver`

## Contribute

To Contribute email <info@robros.dev>

## Snippets
[Wagtail Snippets](https://docs.wagtail.org/en/v4.0.4/topics/snippets.html)
- Content Left
- Content Right
- Full Width Feature
- Subpage Hero Left
- Subpage Hero Right
- Content Aside Left
- Content Aside Right

## Admin Views
[Wagtail Snippets](https://docs.wagtail.org/en/v4.0.4/extending/admin_views.html)
- Ministries
- Staff
- Events | From Cove
- Blog

## Pages
[Wagtail Generic Views?](https://docs.wagtail.org/en/v4.0.4/extending/generic_views.html)
- Beliefs
- Plan a Visit
- Give

### Registering New Admin Menu Item
<https://docs.wagtail.org/en/v4.0.4/reference/hooks.html#construct-main-menu>