# Generated by Django 2.1.5 on 2021-02-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='todolist',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
