# Generated by Django 2.1 on 2018-08-25 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=200)),
                ('genre', models.CharField(blank=True, max_length=120)),
                ('artist', models.CharField(max_length=120)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=120)),
                ('age', models.CharField(max_length=120)),
                ('location', models.CharField(default='my default location', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Album')),
            ],
        ),
    ]
