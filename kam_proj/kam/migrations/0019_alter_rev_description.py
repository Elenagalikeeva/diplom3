# Generated by Django 5.1 on 2024-11-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kam', '0018_rev_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rev',
            name='description',
            field=models.TextField(),
        ),
    ]
