# Generated by Django 3.2.7 on 2022-08-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalize', '0002_auto_20220826_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='name',
            field=models.IntegerField(blank=True, null=True, verbose_name='名前'),
        ),
    ]
