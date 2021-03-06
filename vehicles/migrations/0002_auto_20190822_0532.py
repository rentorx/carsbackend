# Generated by Django 2.1.7 on 2019-08-22 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='account',
            field=models.ForeignKey(default=None, help_text='Account owner for this vehicle', on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
        ),
    ]
