# Generated by Django 3.2.10 on 2023-03-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('emailid', models.EmailField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=15, null=True)),
                ('confirm_password', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
