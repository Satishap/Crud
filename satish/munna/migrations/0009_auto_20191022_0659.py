# Generated by Django 2.2.5 on 2019-10-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munna', '0008_satish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Moblie', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]