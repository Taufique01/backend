# Generated by Django 2.1.7 on 2019-07-13 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deploytodotaskerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('short_description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='drink_images/')),
                ('price', models.IntegerField(default=100)),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploytodotaskerapp.Registration')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deploytodotaskerapp.Drink'),
        ),
    ]
