# Generated by Django 2.1.7 on 2019-06-18 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='vehicle',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicles.Vehicle'),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('user', 'vehicle')},
        ),
    ]
