# Generated by Django 4.1.7 on 2023-03-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file_Upload',
            field=models.FileField(upload_to=''),
        ),
    ]
