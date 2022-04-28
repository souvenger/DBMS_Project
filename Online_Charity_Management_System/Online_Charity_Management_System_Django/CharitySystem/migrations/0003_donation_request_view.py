# Generated by Django 2.1.15 on 2020-06-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharitySystem', '0002_auto_20200617_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_request_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(default=None, max_length=50)),
                ('domain', models.CharField(default=None, max_length=50)),
                ('head_of_ngo', models.CharField(default=None, max_length=50)),
                ('contactNo', models.CharField(default=None, max_length=10)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('donation_description', models.TextField(default=None)),
                ('donation_amount', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'post_request',
                'managed': False,
            },
        ),
    ]
