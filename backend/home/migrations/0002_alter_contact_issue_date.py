# Generated by Django 4.0.3 on 2022-03-24 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='issue_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
