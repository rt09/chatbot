# Generated by Django 3.2.19 on 2023-05-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=100)),
                ('cust_fname', models.CharField(max_length=100)),
                ('cust_lname', models.CharField(max_length=100)),
                ('last_transaction_date', models.DateField(max_length=100)),
                ('ac_balance', models.CharField(max_length=100)),
                ('ac_opening_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.CharField(max_length=100)),
                ('cust_id', models.CharField(max_length=100)),
                ('cross_sell', models.CharField(max_length=100)),
            ],
        ),
    ]