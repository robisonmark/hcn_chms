# Generated by Django 4.0.5 on 2022-10-02 04:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staffpage_family_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpage',
            name='staff_bio',
            field=wagtail.core.fields.StreamField([('staff_bio', wagtail.core.blocks.StructBlock([('staffPosition', wagtail.core.blocks.CharBlock(blank=True, form_classname='Staff Position', required=False)), ('header', wagtail.core.blocks.CharBlock(blank=True, form_classname='Staff Position', required=False))]))], blank=True, null=True),
        ),
    ]