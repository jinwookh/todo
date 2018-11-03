# Generated by Django 2.1 on 2018-11-03 04:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181103_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_title', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField(blank=True, default=0, null=True)),
                ('priority', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]