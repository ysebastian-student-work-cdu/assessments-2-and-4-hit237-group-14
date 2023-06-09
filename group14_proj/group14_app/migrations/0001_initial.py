# Generated by Django 4.2 on 2023-04-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Waste Name', max_length=200, null=True)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('household', 'Household waste'), ('retail', 'Retail waste'), ('restaurant', 'Restaurant waste'), ('agricultural', 'Agricultural waste'), ('processing', 'Processing waste'), ('transportation', 'Transportation and distribution waste')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Student_Id', models.CharField(max_length=10)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Team Members Profile',
            },
        ),
        migrations.CreateModel(
            name='Web_Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brief', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Explanation',
                'verbose_name_plural': 'Website Introduction',
            },
        ),
    ]
