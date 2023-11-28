# Generated by Django 4.2.4 on 2023-10-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reg_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('pin', models.IntegerField(null=True)),
                ('fee_balance', models.FloatField()),
                ('phone', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
