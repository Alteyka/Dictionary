# Generated by Django 2.2.13 on 2020-06-09 11:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dict.BaseModel')),
                ('word_name', models.CharField(max_length=200)),
                ('translate', models.CharField(max_length=200)),
                ('transcription', models.CharField(max_length=200)),
                ('word_in_phrase', models.CharField(max_length=200)),
                ('word_in_sentence', models.CharField(max_length=200)),
            ],
            bases=('dict.basemodel',),
        ),
    ]