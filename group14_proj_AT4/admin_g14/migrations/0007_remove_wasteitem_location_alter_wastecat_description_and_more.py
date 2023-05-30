# Generated by Django 4.2 on 2023-05-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_g14', '0006_wastelog_delete_audit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wasteitem',
            name='location',
        ),
        migrations.AlterField(
            model_name='wastecat',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='wastecat',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]