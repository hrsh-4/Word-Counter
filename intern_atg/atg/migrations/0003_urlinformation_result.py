# Generated by Django 2.2.4 on 2020-01-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atg', '0002_auto_20200127_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlinformation',
            name='result',
            field=models.CharField(default='none', max_length=2048),
            preserve_default=False,
        ),
    ]
