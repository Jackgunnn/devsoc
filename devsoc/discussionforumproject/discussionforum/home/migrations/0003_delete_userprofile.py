# Generated by Django 5.0.3 on 2024-03-18 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
