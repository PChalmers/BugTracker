# Generated by Django 2.2.7 on 2019-12-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='Paul', max_length=64),
            preserve_default=False,
        ),
    ]
