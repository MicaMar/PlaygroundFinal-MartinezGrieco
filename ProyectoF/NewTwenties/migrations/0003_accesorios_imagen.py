# Generated by Django 5.0 on 2023-12-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewTwenties', '0002_textiles_delete_medias'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorios',
            name='imagen',
            field=models.ImageField(null=True, upload_to='accesorios'),
        ),
    ]