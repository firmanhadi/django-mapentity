# Generated by Django 3.2.11 on 2022-01-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_supermarket'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummymodel',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]