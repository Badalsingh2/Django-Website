# Generated by Django 5.0.6 on 2024-06-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0009_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField(max_length=10)),
                ('email_subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
