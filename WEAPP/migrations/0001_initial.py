# Generated by Django 3.2.10 on 2023-03-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='martdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.CharField(blank=True, max_length=40, null=True)),
                ('Image', models.ImageField(upload_to='profile')),
            ],
        ),
    ]
