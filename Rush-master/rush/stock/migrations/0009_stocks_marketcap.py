# Generated by Django 2.1.4 on 2019-08-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20190804_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='marketcap',
            field=models.FloatField(blank='true', null='true'),
            preserve_default='true',
        ),
    ]