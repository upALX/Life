# Generated by Django 4.2.7 on 2023-12-06 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamsSolicitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Under analysis'), ('F', 'Finished')], max_length=2)),
                ('result', models.FileField(blank=True, null=True, upload_to='exams_result')),
                ('password_required', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exams',
            name='exam_datetime',
        ),
        migrations.AlterField(
            model_name='exams',
            name='exam_availability',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='OrderExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_scheduled', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('exams', models.ManyToManyField(to='exams.examssolicitation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='examssolicitation',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exams.exams'),
        ),
        migrations.AddField(
            model_name='examssolicitation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]