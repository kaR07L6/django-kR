# Generated by Django 5.1.4 on 2024-12-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='name',
            field=models.CharField(default='匿名', max_length=100),
        ),
    ]


