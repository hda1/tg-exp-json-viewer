# Generated by Django 3.2 on 2022-05-28 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_auto_20220529_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='name',
        ),
    ]