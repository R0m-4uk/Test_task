# Generated by Django 5.0.2 on 2024-03-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_lesson_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True, verbose_name='url'),
        ),
    ]
