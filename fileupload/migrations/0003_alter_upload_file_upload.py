# Generated by Django 4.1.7 on 2023-03-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_alter_upload_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file_Upload',
            field=models.FileField(upload_to='image'),
        ),
    ]