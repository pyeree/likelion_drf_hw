# Generated by Django 5.0.6 on 2024-07-05 09:53

import django.db.models.deletion
import music.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=300)),
                ('debut', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=music.models.image_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('release', models.DateField()),
                ('content', models.TextField(max_length=300)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.singer')),
            ],
        ),
        migrations.AddField(
            model_name='singer',
            name='tag',
            field=models.ManyToManyField(blank=True, to='music.tag'),
        ),
    ]
