# Generated by Django 2.2.2 on 2019-06-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='bodyvital',
            name='prescription',
        ),
    ]
