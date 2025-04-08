# Generated by Django 4.1.7 on 2024-11-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gymapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='product')),
                ('desc', models.CharField(max_length=1500)),
            ],
        ),
    ]
