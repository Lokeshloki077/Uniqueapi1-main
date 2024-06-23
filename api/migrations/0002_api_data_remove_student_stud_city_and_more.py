# Generated by Django 4.2.6 on 2024-03-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'api_data',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='stud_city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stud_course',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]