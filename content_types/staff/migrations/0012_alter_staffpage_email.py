# Generated by Django 4.0.5 on 2023-07-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_staffpage_component_staffpage_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpage',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]