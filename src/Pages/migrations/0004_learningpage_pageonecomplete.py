# Generated by Django 2.1.5 on 2021-02-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_filestore_learningpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpage',
            name='pageOneComplete',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
