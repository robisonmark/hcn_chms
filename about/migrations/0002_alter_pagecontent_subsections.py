# Generated by Django 4.0.5 on 2022-06-21 00:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='subsections',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(blank=True, form_classname='Section Header', required=False)), ('displayHeader', wagtail.core.blocks.BooleanBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(Required=True, help_text='Add the page content here')), ('isHeaderLink', wagtail.core.blocks.BooleanBlock(form_classname='Is Header a Link', required=False)), ('headerLink', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]
