# Generated by Django 3.2.2 on 2021-05-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ref_groupaccess',
            name='name',
        ),
        migrations.AddField(
            model_name='ref_groupaccess',
            name='access_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ref_groupaccess',
            name='group_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
