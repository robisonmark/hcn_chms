# Generated by Django 4.0.5 on 2022-10-08 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('staff', '0008_staffpage_test_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffpage',
            name='ministry_links',
        ),
        migrations.RemoveField(
            model_name='staffpage',
            name='test_link',
        ),
        migrations.AddField(
            model_name='staffpage',
            name='ministry_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
