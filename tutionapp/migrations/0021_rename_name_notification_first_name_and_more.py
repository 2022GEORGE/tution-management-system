# Generated by Django 4.2.4 on 2023-10-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutionapp', '0020_assignmenttable_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='notificationtable',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='notificationtable',
            name='userid',
        ),
        migrations.AddField(
            model_name='notification',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='contact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notificationtable',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notificationtable',
            name='user_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='notificationtable',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
