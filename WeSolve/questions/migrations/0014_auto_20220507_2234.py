# Generated by Django 3.0.8 on 2022-05-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20220507_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(default='', max_length=240),
        ),
    ]
