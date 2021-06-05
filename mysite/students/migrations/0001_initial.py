# Generated by Django 3.2 on 2021-05-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('sex', models.BooleanField(default=True, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('class_num', models.CharField(max_length=5, verbose_name='班级编号')),
                ('description', models.TextField(max_length=1000, verbose_name='个性签名')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'tb_students',
            },
        ),
    ]