# Generated by Django 4.2.4 on 2023-10-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0021_rename_name_notification_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passtable',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutionapp.notification'),
        ),
    ]
