# Generated by Django 2.2.3 on 2019-09-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0006_auto_20190906_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chest_pain',
            name='improves_with',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='chest_pain',
            name='worsens_with',
            field=models.CharField(max_length=2000),
        ),
    ]
