# Generated by Django 3.0.4 on 2020-03-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kensaku', '0002_auto_20200321_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='group',
            field=models.CharField(default=0, max_length=25, verbose_name='ジャンル'),
            preserve_default=False,
        ),
    ]