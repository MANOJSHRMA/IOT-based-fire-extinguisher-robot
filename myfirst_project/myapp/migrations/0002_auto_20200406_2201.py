# Generated by Django 2.2.2 on 2020-04-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firerecords',
            name='phone_number',
            field=models.CharField(default='+14372185806', max_length=20),
        ),
        migrations.AddField(
            model_name='firerecords',
            name='sms_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='firerecords',
            name='sms_text',
            field=models.CharField(default='no text', max_length=255),
        ),
    ]
