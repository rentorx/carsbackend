# Generated by Django 2.1.7 on 2019-08-22 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Last modified at')),
                ('is_fraud', models.BooleanField(db_index=True, default=False, help_text='Marks if the user is trying to cheat the system.', verbose_name='Is fraud')),
                ('is_company', models.BooleanField(db_index=True, default=False, help_text='Marks if the user is owner is a service provider.', verbose_name='Is company')),
                ('company', models.ForeignKey(default=None, help_text='Companies related to this account', on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
