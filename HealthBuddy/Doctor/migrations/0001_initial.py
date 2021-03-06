
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DayAndTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('visitDay', models.ManyToManyField(to='Doctor.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HCDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatmentFor', models.TextField(blank=True)),
                ('remarks', models.TextField(blank=True)),
                ('roomNo7', models.TextField(blank=True)),
                ('med_added', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='TestList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks_from_doc', models.TextField(blank=True)),
                ('remarks_to_doc', models.TextField(blank=True)),
                ('from_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_doc', to='Doctor.Doctor')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
                ('to_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_doc', to='Doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PresMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=100)),
                ('times_a_day', models.PositiveIntegerField()),
                ('no_of_days', models.PositiveIntegerField()),
                ('when_to_take', models.CharField(choices=[('b', 'Before meal'), ('a', 'After meal'), ('n', 'Night')], default='a', max_length=1)),
                ('provided', models.BooleanField(default=False)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
        migrations.CreateModel(
            name='PresDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Doctor')),
                ('pres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='tests',
            field=models.ManyToManyField(blank=True, to='Doctor.TestList'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.HCDept'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='visit_day_time',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Doctor.DayAndTime'),
        ),
    ]
