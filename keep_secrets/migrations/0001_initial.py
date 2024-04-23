# Generated by Django 5.0.4 on 2024-04-23 11:34

import keep_secrets.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', keep_secrets.models.EncryptedTextField()),
                ('code', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': 'секрет',
                'verbose_name_plural': 'секреты',
            },
        ),
    ]