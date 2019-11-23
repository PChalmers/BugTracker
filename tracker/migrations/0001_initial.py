# Generated by Django 2.2.7 on 2019-11-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('owner', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='recordComment',
            fields=[
                ('commentID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('content', models.CharField(blank=True, max_length=256, null=True)),
                ('owner', models.EmailField(max_length=254)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('owner', models.EmailField(max_length=254)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField()),
                ('status', models.CharField(choices=[('IN', 'Initial'), ('OP', 'Opened'), ('BL', 'Blocked'), ('CL', 'Closed')], default='IN', max_length=2)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.recordComment')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.project')),
            ],
        ),
    ]
