# Generated by Django 3.1.5 on 2021-04-03 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20210402_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('id_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.list_blog')),
            ],
        ),
    ]
