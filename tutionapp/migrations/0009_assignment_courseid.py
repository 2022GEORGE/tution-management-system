# Generated by Django 4.2.4 on 2023-10-16 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0008_assignment_assignmenttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='courseid',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tutionapp.course'),
            preserve_default=False,
        ),
    ]
