# Generated by Django 4.2.5 on 2023-09-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(default='media/profile_img.webp', null=True, upload_to='images/'),
        ),
    ]
