# Generated by Django 2.2.13 on 2020-06-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='word_in_phrase',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_in_sentence',
            new_name='phrase',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_name',
            new_name='sentence',
        ),
    ]
