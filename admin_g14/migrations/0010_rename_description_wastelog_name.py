# Generated by Django 4.2 on 2023-05-29 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_g14', '0009_remove_user_role_delete_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wastelog',
            old_name='description',
            new_name='name',
        ),
    ]
