# Generated by Django 3.1.7 on 2021-04-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(max_length=80, unique=True)),
                ('apps', models.CharField(max_length=80, unique=True)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]