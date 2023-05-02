# Generated by Django 4.2 on 2023-05-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='degree',
            field=models.CharField(choices=[('ปริญญาตรี', 'ปริญญาตรี'), ('ปริญญาโท', 'ปริญญาโท'), ('ปริญญาเอก', 'ปริญญาเอก')], default='ปริญญาตรี', max_length=40),
        ),
    ]