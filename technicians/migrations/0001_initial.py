# Generated by Django 2.2.1 on 2019-05-25 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machines', '0002_auto_20190525_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('noti_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ไอดีการแจ้งเตือน')),
                ('user_send', models.CharField(max_length=50, verbose_name='ผู้แจ้งเสีย')),
                ('user_receive', models.CharField(max_length=50, null=True, verbose_name='ผู้รับแจ้ง')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='วันที่แจ้ง')),
                ('fix_description_extra', models.TextField(verbose_name='สาเหตุการเสีย')),
                ('work_status', models.PositiveSmallIntegerField(choices=[(1, 'มีการแจ้งเตือน'), (2, 'มอบหมายให้ช่าง'), (3, 'ซ่อมเรียบร้อย'), (4, 'ซ่อมไม่ได้')], default=1, verbose_name='สถานะของงาน')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='branches.Branch', verbose_name='สาขา')),
                ('machine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.BranchMachine', verbose_name='เครื่องที่เสีย')),
            ],
            options={
                'verbose_name': 'จัดการการซ่อม',
                'verbose_name_plural': 'จัดการการซ่อม',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ไอดีการซ่อมเสีย')),
                ('confirm_photo', models.ImageField(max_length=60, upload_to='confirm_photo/', verbose_name='รูปถ่ายการซ่อม')),
                ('todo_date', models.DateTimeField(auto_now_add=True, verbose_name='วันที่มอบหมายงาน')),
                ('finish_date', models.DateTimeField(auto_now=True, verbose_name='วันที่เสร็จงาน')),
                ('comment', models.CharField(blank=True, help_text='ถ้ามี', max_length=60, null=True, verbose_name='ข้อคิดเห็น')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='ค่าใช้จ่าย')),
                ('work_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'กำลังดำเนินการ'), (2, 'ซ่อมเรียบร้อย'), (3, 'ซ่อมไม่ได้')], default=1, null=True, verbose_name='สถานะของงาน')),
                ('tech_name', models.ForeignKey(limit_choices_to={'user_type': 4}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ชื่อช่างที่ซ่อม')),
                ('work_fix', models.ForeignKey(limit_choices_to={'work_status': 2}, on_delete=django.db.models.deletion.CASCADE, to='technicians.Notification', verbose_name='สาเหตุ')),
                ('work_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.Branch', verbose_name='สาขาที่ซ่อม')),
                ('work_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.BranchMachine', verbose_name='เครื่องที่ซ่อม')),
            ],
            options={
                'verbose_name': 'งานของช่าง',
                'verbose_name_plural': 'งานของช่าง',
            },
        ),
        migrations.CreateModel(
            name='MachineMaintained',
            fields=[
                ('maintaine_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ไอดีการซ่อม')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='วันที่มอบหมายงาน')),
                ('comment', models.CharField(blank=True, help_text='ถ้ามี', max_length=60, null=True, verbose_name='ข้อคิดเห็น')),
                ('work', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'งานซ่อมทั่วไป'), (2, 'งานซ่อมบำรุง')], null=True, verbose_name='ประเภทของงาน')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='ค่าใช้จ่าย')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'มอบหมายงานแล้ว'), (2, 'ซ่อมเรียบร้อย'), (3, 'ซ่อมไม่ได้')], default=1, null=True, verbose_name='สถานะของงาน')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.Branch', verbose_name='สาขา')),
                ('tech_name', models.ForeignKey(limit_choices_to={'user_type': 4}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ชื่อช่างที่ซ่อม')),
            ],
        ),
    ]
