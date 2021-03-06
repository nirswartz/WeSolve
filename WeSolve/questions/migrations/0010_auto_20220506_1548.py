# Generated by Django 3.0.8 on 2022-05-06 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0009_question_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default='cdf09df6-6e9e-42b0-928b-b119ce4f86bb', limit_choices_to={'isTeacher': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
