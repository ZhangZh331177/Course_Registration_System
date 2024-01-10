# Generated by Django 2.2.11 on 2024-01-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20240109_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.IntegerField(choices=[(1, '第一节'), (2, '第二节'), (3, '第三节'), (4, '第四节'), (5, '第五节'), (6, '第六节'), (7, '第七节'), (8, '第八节')], default=1, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_week',
            field=models.IntegerField(choices=[(1, '第一周'), (2, '第二周'), (3, '第三周'), (4, '第四周'), (5, '第五周'), (6, '第六周'), (7, '第七周'), (8, '第八周')], default=1, verbose_name='结束周'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_week',
            field=models.IntegerField(choices=[(1, '第一周'), (2, '第二周'), (3, '第三周'), (4, '第四周'), (5, '第五周'), (6, '第六周'), (7, '第七周'), (8, '第八周')], default=1, verbose_name='开始周'),
        ),
    ]
