# Generated by Django 4.2.4 on 2023-10-16 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0006_passtable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='courseid',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='course',
            new_name='courseid',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='department',
            new_name='departmentid',
        ),
    ]
