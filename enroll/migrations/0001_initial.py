# Generated by Django 4.0.4 on 2022-04-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
