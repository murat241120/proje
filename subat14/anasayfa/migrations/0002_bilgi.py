# Generated by Django 3.2.12 on 2022-03-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bilgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogrenci_bilgi', models.CharField(max_length=100)),
            ],
        ),
    ]
