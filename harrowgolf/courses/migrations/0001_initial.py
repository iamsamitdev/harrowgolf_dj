# Generated by Django 4.2.2 on 2023-06-26 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('remark', models.CharField(blank=True, max_length=255)),
                ('school_id', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.IntegerField()),
            ],
        ),
    ]
