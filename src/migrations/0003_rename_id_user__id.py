# Generated by Django 4.1.5 on 2023-01-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_remove_user_emailid_remove_user_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='_id',
        ),
    ]
