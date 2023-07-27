# Generated by Django 4.2.3 on 2023-07-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=256)),
                ('hash', models.CharField(max_length=10)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
            ],
        ),
    ]
