# Generated by Django 3.2.7 on 2021-10-08 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp3', '0005_alter_myuser_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='father',
            new_name='father_name',
        ),
    ]