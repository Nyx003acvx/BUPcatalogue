# Generated by Django 5.1.3 on 2025-01-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowerFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads/flowers/')),
            ],
        ),
    ]
