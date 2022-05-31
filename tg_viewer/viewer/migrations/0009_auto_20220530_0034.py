# Generated by Django 3.2 on 2022-05-29 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_auto_20220529_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='message',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='viewer.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(default='', max_length=700, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='message',
            name='visibility',
            field=models.BooleanField(blank=True, null=True, verbose_name='Видимость'),
        ),
    ]