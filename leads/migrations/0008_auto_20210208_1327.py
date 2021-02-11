# Generated by Django 3.1.5 on 2021-02-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20210208_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='leads.category'),
        ),
    ]
