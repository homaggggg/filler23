# Generated by Django 4.2.7 on 2023-12-11 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID', primary_key=True, serialize=False)),
                ('createdate', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
