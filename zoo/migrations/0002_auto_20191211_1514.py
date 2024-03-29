# Generated by Django 3.0 on 2019-12-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animalStatus',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='animalType',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='healthPercentage',
        ),
        migrations.AddField(
            model_name='elephant',
            name='animalStatus',
            field=models.CharField(default='COMPLETELY HEALTHY', max_length=32),
        ),
        migrations.AddField(
            model_name='elephant',
            name='animalType',
            field=models.CharField(default='Elephant', max_length=32),
        ),
        migrations.AddField(
            model_name='elephant',
            name='healthPercentage',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='gorilla',
            name='animalStatus',
            field=models.CharField(default='COMPLETELY HEALTHY', max_length=32),
        ),
        migrations.AddField(
            model_name='gorilla',
            name='animalType',
            field=models.CharField(default='Gorilla', max_length=32),
        ),
        migrations.AddField(
            model_name='gorilla',
            name='healthPercentage',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='monkey',
            name='animalStatus',
            field=models.CharField(default='COMPLETELY HEALTHY', max_length=32),
        ),
        migrations.AddField(
            model_name='monkey',
            name='animalType',
            field=models.CharField(default='Monkey', max_length=32),
        ),
        migrations.AddField(
            model_name='monkey',
            name='healthPercentage',
            field=models.FloatField(default=100),
        ),
    ]
