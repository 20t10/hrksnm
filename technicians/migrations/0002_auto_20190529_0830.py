# Generated by Django 2.2.1 on 2019-05-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicians', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='work_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'มีการแจ้งเตือน'), (2, 'มอบหมายให้ช่าง'), (3, 'ซ่อมเรียบร้อย'), (4, 'ซ่อมไม่ได้'), (5, 'ยกเลิกการแจ้งเตือน')], default=1, verbose_name='สถานะของงาน'),
        ),
    ]