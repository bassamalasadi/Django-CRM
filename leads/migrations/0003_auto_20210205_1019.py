# Generated by Django 3.1.5 on 2021-02-05 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210205_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
