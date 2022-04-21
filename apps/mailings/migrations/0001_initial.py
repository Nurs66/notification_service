# Generated by Django 4.0.4 on 2022-04-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Mailing start')),
                ('date_end', models.DateTimeField(verbose_name='End of mailing')),
                ('time_start', models.TimeField(verbose_name='Start time to send message')),
                ('time_end', models.TimeField(verbose_name='End time to send message')),
                ('text', models.TextField(verbose_name='Message text')),
                ('tag', models.CharField(max_length=100, verbose_name='Search by tags')),
                ('mobile_operator_code', models.CharField(max_length=5, verbose_name='Search by mobile operator code')),
            ],
            options={
                'verbose_name': 'Mailing',
                'verbose_name_plural': 'Mailings',
                'ordering': ('-id',),
            },
        ),
    ]