# Generated by Django 4.0 on 2022-02-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userdetail_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(None, 'Please select drink type'), ('S', 'Americano'), ('M', 'Capuccino'), ('L', 'Cold Brew Coffee')], max_length=10)),
                ('size', models.CharField(choices=[(None, 'Please select a size'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=10)),
                ('quantity', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=10)),
            ],
        ),
    ]
