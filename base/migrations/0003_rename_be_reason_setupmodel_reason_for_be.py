# Generated by Django 4.0.1 on 2022-04-30 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_setupmodel_be_setupmodel_sl_setupmodel_tp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setupmodel',
            old_name='be_reason',
            new_name='Reason_For_be',
        ),
    ]
