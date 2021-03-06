# Generated by Django 3.2.2 on 2021-05-14 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210513_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='books',
            name='type_id',
        ),
        migrations.RemoveField(
            model_name='ref_bookauthor',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='ref_bookauthor',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='ref_booktags',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='ref_booktags',
            name='tag_id',
        ),
        migrations.RemoveField(
            model_name='ref_groupaccess',
            name='access_id',
        ),
        migrations.RemoveField(
            model_name='ref_groupaccess',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='ref_useraccess',
            name='access_id',
        ),
        migrations.RemoveField(
            model_name='ref_useraccess',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='ref_usergroup',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='ref_usergroup',
            name='user_id',
        ),
        migrations.AddField(
            model_name='books',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.book_types'),
        ),
        migrations.AddField(
            model_name='ref_bookauthor',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.book_authors'),
        ),
        migrations.AddField(
            model_name='ref_bookauthor',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.books'),
        ),
        migrations.AddField(
            model_name='ref_booktags',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.books'),
        ),
        migrations.AddField(
            model_name='ref_booktags',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.book_tags'),
        ),
        migrations.AddField(
            model_name='ref_groupaccess',
            name='access',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.baccess'),
        ),
        migrations.AddField(
            model_name='ref_groupaccess',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bgroups'),
        ),
        migrations.AddField(
            model_name='ref_useraccess',
            name='access',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.baccess'),
        ),
        migrations.AddField(
            model_name='ref_useraccess',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.busers'),
        ),
        migrations.AddField(
            model_name='ref_usergroup',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bgroups'),
        ),
        migrations.AddField(
            model_name='ref_usergroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.busers'),
        ),
    ]
