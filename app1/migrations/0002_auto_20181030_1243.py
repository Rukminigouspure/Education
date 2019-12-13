# Generated by Django 2.1.2 on 2018-10-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('coursename', models.CharField(max_length=40)),
                ('courseid', models.IntegerField(default=6, primary_key=True, serialize=False)),
                ('coursefee', models.IntegerField(default=6)),
                ('courseduration', models.IntegerField(default=4)),
            ],
        ),
        migrations.DeleteModel(
            name='course',
        ),
    ]
