# Generated by Django 3.0.8 on 2022-05-06 12:27

from django.db import migrations, models
import questions.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_answer_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answerPic',
            field=models.ImageField(blank=True, default='', upload_to=questions.models.Answer.upload_location),
        ),
    ]