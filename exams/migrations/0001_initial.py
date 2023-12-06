# Generated by Django 4.2.7 on 2023-12-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('exam_type', models.CharField(choices=[('H', 'Hemograma exam'), ('C', 'Colesterol'), ('G', 'Glicose'), ('I', 'Ionograma'), ('X', 'Raio-X')], max_length=1)),
                ('exam_price', models.FloatField()),
                ('exam_availability', models.BooleanField(default=False)),
                ('exam_datetime', models.DateTimeField()),
            ],
        ),
    ]
