# Generated by Django 2.2.5 on 2019-09-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
