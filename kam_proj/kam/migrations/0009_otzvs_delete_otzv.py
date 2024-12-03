# Generated by Django 5.1 on 2024-11-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kam', '0008_rename_reviews_otzv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otzvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Otzv',
        ),
    ]
