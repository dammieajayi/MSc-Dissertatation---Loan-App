# Generated by Django 4.1.4 on 2022-12-21 00:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbvn',
            name='reference',
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
