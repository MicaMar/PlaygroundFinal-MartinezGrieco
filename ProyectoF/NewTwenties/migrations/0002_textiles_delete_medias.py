# Generated by Django 5.0 on 2023-12-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewTwenties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Medias',
        ),
    ]
