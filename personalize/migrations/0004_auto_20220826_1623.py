# Generated by Django 3.2.7 on 2022-08-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalize', '0003_alter_tea_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='base',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ベース'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms10',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms11',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms12',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms13',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms14',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms15',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms6',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms7',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms8',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='symptoms9',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='症状'),
        ),
    ]
