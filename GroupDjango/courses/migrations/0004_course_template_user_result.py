# Generated by Django 4.1 on 2022-09-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='template_user_result',
            field=models.SmallIntegerField(default=0),
        ),
    ]