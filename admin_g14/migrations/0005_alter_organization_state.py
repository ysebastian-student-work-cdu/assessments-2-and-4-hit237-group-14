# Generated by Django 4.2 on 2023-05-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_g14', '0004_role_organization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='state',
            field=models.CharField(choices=[('ACT', 'Australian Capital Territory'), ('VIC', 'Victoria'), ('NSW', 'New South Wales'), ('WA', 'WA'), ('NT', 'NT'), ('QLD', 'QLD')], max_length=10),
        ),
    ]