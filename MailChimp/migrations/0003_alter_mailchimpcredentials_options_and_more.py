# Generated by Django 4.0.1 on 2022-01-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MailChimp', '0002_mailchimpcredentials'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailchimpcredentials',
            options={'verbose_name_plural': 'Mail Chimp Credentials'},
        ),
        migrations.AddField(
            model_name='mailchimpcredentials',
            name='callback',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
