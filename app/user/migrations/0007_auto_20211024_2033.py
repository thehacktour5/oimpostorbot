# Generated by Django 3.2.7 on 2021-10-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_usermodel_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='points',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.DeleteModel(
            name='PointsUser',
        ),
    ]