# Generated by Django 4.2.4 on 2023-10-01 20:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBar', '0002_contactmessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='MensajeContacto',
        ),
    ]