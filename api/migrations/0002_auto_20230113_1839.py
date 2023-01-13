# Generated by Django 3.2.5 on 2023-01-13 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chant',
            name='published_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chant',
            name='paroles',
            field=models.TextField(max_length=3000),
        ),
    ]