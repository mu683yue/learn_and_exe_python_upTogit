# Generated by Django 2.2 on 2019-04-21 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.Event'),
        ),
    ]
