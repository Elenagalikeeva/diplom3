# Generated by Django 5.1 on 2024-11-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kam', '0002_slide_alter_kam_description_alter_kam_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='More',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='kam/image/')),
                ('price', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Obzor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='kam/image/')),
                ('price', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vosho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='kam/image/')),
                ('price', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='kam/image/')),
                ('price', models.CharField(max_length=300)),
            ],
        ),
    ]
