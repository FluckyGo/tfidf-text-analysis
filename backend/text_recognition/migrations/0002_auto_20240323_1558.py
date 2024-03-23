# Generated by Django 3.2.16 on 2024-03-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_recognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='inverse_document_frequency',
            field=models.IntegerField(verbose_name='Oбратная частота документа или IDF'),
        ),
        migrations.AlterField(
            model_name='text',
            name='term_frequency',
            field=models.IntegerField(verbose_name='Частота слова или TF'),
        ),
    ]