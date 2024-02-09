# Generated by Django 3.2.22 on 2023-10-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_passwordreset', '0003_allow_blank_and_null_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpasswordtoken',
            name='user_agent',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='HTTP User Agent'),
        ),
    ]