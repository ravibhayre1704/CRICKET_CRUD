# Generated by Django 4.1.1 on 2022-09-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]