# Generated by Django 2.2 on 2021-06-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
                ('url', models.URLField()),
            ],
        ),
    ]
