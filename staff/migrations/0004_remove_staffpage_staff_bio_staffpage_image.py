# Generated by Django 4.0.5 on 2022-10-02 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('staff', '0003_staffpage_staff_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffpage',
            name='staff_bio',
        ),
        migrations.AddField(
            model_name='staffpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
