# Generated by Django 4.0.5 on 2022-10-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpage',
            name='family_name',
            field=models.CharField(default='Family Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='given_name',
            field=models.CharField(default='Given Name', max_length=100),
        ),
    ]