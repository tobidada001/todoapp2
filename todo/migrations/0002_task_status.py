# Generated by Django 4.1 on 2022-09-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
            preserve_default=False,
        ),
    ]
