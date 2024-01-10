# Generated by Django 2.2.11 on 2024-01-09 09:50

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20240109_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[user.models.validate_length], verbose_name='教职工号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[user.models.validate_stu_length], verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[user.models.validate_length], verbose_name='教职工号'),
        ),
    ]
