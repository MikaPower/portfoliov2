# Generated by Django 2.2.4 on 2019-08-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='wtf', max_length=255),
            preserve_default=False,
        ),
    ]
