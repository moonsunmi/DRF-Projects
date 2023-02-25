# Generated by Django 4.1.7 on 2023-02-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_important', models.BooleanField(default=False)),
            ],
        ),
    ]
