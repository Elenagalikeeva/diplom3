# Generated by Django 5.1 on 2024-11-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kam', '0019_alter_rev_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rev',
            name='image',
            field=models.ImageField(blank=True, upload_to='kam/image/'),
        ),
    ]
