# Generated by Django 3.0.5 on 2021-02-03 23:38

import api.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('identifier', models.IntegerField()),
                ('course_title', models.CharField(max_length=200)),
                ('num_subscribers', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('attachment', models.CharField(max_length=200)),
                ('courses', djongo.models.fields.ArrayField(model_container=api.models.Course)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.IntegerField()),
                ('courses', djongo.models.fields.ArrayField(model_container=api.models.Course)),
            ],
        ),
    ]