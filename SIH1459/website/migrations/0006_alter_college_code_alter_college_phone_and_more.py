# Generated by Django 5.0 on 2023-12-19 10:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_scheme_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='code',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(5)], verbose_name='College Code'),
        ),
        migrations.AlterField(
            model_name='college',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='College Phone'),
        ),
        migrations.AlterField(
            model_name='college',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)], verbose_name='College Pincode'),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(3)], verbose_name='Course Code'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(3)], verbose_name='Scheme Id'),
        ),
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.CharField(max_length=2, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(2)], verbose_name='State Code'),
        ),
        migrations.AlterField(
            model_name='student',
            name='aadhar_id',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)], verbose_name='Aadhar ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_year',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(2)], verbose_name='Admission Year'),
        ),
        migrations.AlterField(
            model_name='student',
            name='scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.scheme'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(13), django.core.validators.MaxLengthValidator(13)], verbose_name='UID'),
        ),
    ]
