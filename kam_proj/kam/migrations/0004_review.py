# Generated by Django 5.1 on 2024-11-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kam', '0003_more_obzor_vosho_vse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
