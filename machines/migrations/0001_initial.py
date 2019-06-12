# Generated by Django 2.2.1 on 2019-05-25 02:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(help_text='ชื่อสาขา ตามด้วยเลข 01-99', max_length=60, verbose_name='ชื่อ เครื่อง')),
                ('machine_repair', models.DateTimeField(auto_now_add=True, verbose_name='วันที่ซ่อม')),
                ('next_fix', models.DateTimeField(default=datetime.datetime(2019, 10, 22, 9, 42, 44, 538795), verbose_name='การซ่อมครั้งถัดไป')),
                ('machine_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='branches.Branch', verbose_name='สาขา')),
            ],
            options={
                'verbose_name': 'เครื่องของสาขา',
                'verbose_name_plural': 'เครื่องของสาขา',
            },
        ),
        migrations.CreateModel(
            name='MachineReal',
            fields=[
                ('real_id', models.IntegerField(primary_key=True, serialize=False)),
                ('real_thb', models.DecimalField(decimal_places=2, max_digits=12)),
                ('real_date', models.DateField(auto_now_add=True)),
                ('real_time', models.TimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.BranchMachine')),
            ],
            options={
                'db_table': 'realtime_module',
            },
        ),
        migrations.CreateModel(
            name='MachineLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_thb', models.DecimalField(decimal_places=2, max_digits=12)),
                ('log_module', models.CharField(max_length=32)),
                ('log_date', models.DateField(auto_now_add=True)),
                ('log_time', models.TimeField(auto_now_add=True)),
                ('log_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.Branch')),
            ],
            options={
                'db_table': 'log_module',
            },
        ),
    ]
