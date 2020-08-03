# Generated by Django 3.0.9 on 2020-08-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('term', models.CharField(choices=[('Fall 2020', 'Fall 2020'), ('Spring 2021', 'Spring 2021')], default='Fall 2020', max_length=100)),
                ('instructor', models.CharField(max_length=500)),
                ('uclass_id', models.CharField(default='none', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('shortname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField(max_length=500)),
                ('uClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.uClass')),
            ],
        ),
        migrations.AddField(
            model_name='uclass',
            name='uni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.University'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('uClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.uClass')),
            ],
        ),
    ]