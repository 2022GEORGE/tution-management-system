# Generated by Django 4.2.4 on 2023-10-23 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0024_attendancereport_courseid'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='courseid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutionapp.course'),
        ),
    ]
