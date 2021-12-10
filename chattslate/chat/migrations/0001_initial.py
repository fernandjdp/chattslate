# Generated by Django 4.0 on 2021-12-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('script', models.TextField(blank=True, null=True)),
                ('chat_begin_datetime', models.DateTimeField(auto_now_add=True)),
                ('chat_end_datetime', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(null=True)),
            ],
        ),
    ]