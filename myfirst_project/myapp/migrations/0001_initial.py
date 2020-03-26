# Generated by Django 2.2.2 on 2020-03-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FireRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='manoj sharma', max_length=30)),
                ('email', models.EmailField(default='manoj2sharma1996@gmail.com', max_length=254)),
                ('Alarm_status', models.BooleanField(default=False)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
