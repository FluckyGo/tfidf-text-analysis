# Generated by Django 3.2.16 on 2024-03-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_recognition', '0006_auto_20240324_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='term_frequency',
            field=models.FloatField(default=0, verbose_name='Частота слова или TF'),
        ),
    ]
