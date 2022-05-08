# Generated by Django 4.0.1 on 2022-05-06 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SetUpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('schema', models.CharField(choices=[('Basket Indices', 'Basket Indices'), ('Bond', 'Bond'), ('Cryptocurrencies', 'Cryptocurrencies'), ('Economy', 'Economy'), ('Forex', 'Forex'), ('Futures Indices', 'Futures Indices'), ('Stock Indices', 'Stock Indices'), ('Synthetic Indices', 'Synthetic Indices')], max_length=50)),
                ('Asset_Name', models.CharField(max_length=50)),
                ('Image_before', models.ImageField(upload_to='setup_Model/%Y/%m/%d')),
                ('Image_before2', models.ImageField(blank=True, null=True, upload_to='setup_Model/%Y/%m/%d')),
                ('bias', models.TextField()),
                ('Image_after', models.ImageField(blank=True, null=True, upload_to='setup_Model/%Y/%m/%d')),
                ('Image_after2', models.ImageField(blank=True, null=True, upload_to='setup_Model/%Y/%m/%d')),
                ('result', models.CharField(blank=True, choices=[('Tp', 'Tp'), ('Sl', 'Sl')], max_length=10, null=True)),
                ('be', models.BooleanField(default=False, verbose_name='be')),
                ('Reason_For_be', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
