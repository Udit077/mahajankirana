# Generated by Django 3.0.3 on 2021-03-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_series_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(default=0)),
            ],
        ),
    ]
