# Generated by Django 5.0 on 2023-12-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(verbose_name='Course Duration'),
        ),
    ]
