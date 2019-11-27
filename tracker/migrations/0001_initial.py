# Generated by Django 2.2.7 on 2019-11-27 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('accountID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=32)),
                ('description', models.CharField(blank=True, default='', max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('priority', models.CharField(choices=[('AD', 'Admin'), ('L1', 'Level1'), ('L2', 'Level2'), ('L3', 'Locked')], default='L1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=32)),
                ('description', models.CharField(blank=True, default='', max_length=256)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.account')),
            ],
        ),
        migrations.CreateModel(
            name='recordComment',
            fields=[
                ('commentID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=32)),
                ('content', models.CharField(blank=True, default='', max_length=256)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.account')),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('RE', 'Requirement'), ('DE', 'Defect'), ('BD', 'Build'), ('WK', 'Work')], default='WK', max_length=2)),
                ('status', models.CharField(choices=[('IN', 'Initial'), ('OP', 'Opened'), ('BL', 'Blocked'), ('RE', 'Resolved'), ('CL', 'Closed')], default='IN', max_length=2)),
                ('title', models.CharField(blank=True, default='', max_length=32)),
                ('description', models.CharField(blank=True, default='', max_length=256)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('resolution', models.CharField(blank=True, default='', max_length=256)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned', to='tracker.account')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.recordComment')),
                ('originator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='originator', to='tracker.account')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.project')),
            ],
        ),
    ]
