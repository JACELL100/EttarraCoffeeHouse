# Generated by Django 5.1.2 on 2024-10-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('sno', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('sno', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('id', models.IntegerField(unique=True)),
                ('event', models.CharField(default='Music', max_length=100)),
                ('price', models.IntegerField(default=500)),
                ('purchased_by', models.CharField(max_length=50)),
                ('numberoftickets', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('sno', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Mark', max_length=50)),
                ('email', models.CharField(default='helloworld', max_length=50)),
                ('password', models.CharField(default='12345678', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('gprice', models.DecimalField(decimal_places=2, default=500, max_digits=10)),
                ('VIPrice', models.DecimalField(decimal_places=2, default=500, max_digits=10)),
                ('theme', models.TextField(default='NA')),
                ('venue', models.TextField(default='NA')),
                ('chef', models.CharField(default='NA', max_length=50)),
                ('date', models.DateField(default=None)),
                ('time', models.TimeField(default=None)),
                ('seats', models.PositiveIntegerField(default=0)),
                ('details', models.TextField(default='NA')),
            ],
        ),
    ]
