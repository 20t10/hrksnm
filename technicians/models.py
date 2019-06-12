
from django.db import models
from branches.models import Branch
from machines.models import BranchMachine
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


# anybody send this is broken นี่คือส่ง
class Notification(models.Model):
    noti_id = models.AutoField(primary_key=True, verbose_name="ไอดีการแจ้งเตือน")
    user_send = models.CharField(verbose_name='ผู้แจ้งเสีย',max_length=50,)
    user_receive = models.CharField(verbose_name='ผู้รับแจ้ง',max_length=50,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True, verbose_name='สาขา')
    machine = models.ForeignKey(BranchMachine,
                                on_delete=models.SET_NULL, null=True,
                                verbose_name='เครื่องที่เสีย')#status = true
    send_date = models.DateTimeField(verbose_name = 'วันที่แจ้ง',auto_now_add=True,auto_now=False)
    fix_description_extra = models.TextField( verbose_name = 'สาเหตุการเสีย')
    STATUS_CHOICES = (
        (1, 'มีการแจ้งเตือน'),
        (2, 'มอบหมายให้ช่าง'),
        (3, 'ซ่อมเรียบร้อย'),
        (4, 'ซ่อมไม่ได้'),
        (5, 'ยกเลิกการแจ้งเตือน'),
    )
    work_status = models.PositiveSmallIntegerField(verbose_name = 'สถานะของงาน',choices=STATUS_CHOICES,default=1)#confirm by admin

    def __str__(self):
        return 'สาเหตุ %s  เครื่อง %s' %(
                               self.fix_description_extra,
                               self.machine.machine_name,
                               )
    class Meta:
        verbose_name = 'จัดการการซ่อม'
        verbose_name_plural = 'จัดการการซ่อม'

# admin staff -> tech create update=confirmwork_status work5status this is repair นี่คือซ่อม
class TodoList(models.Model):
    todo_id = models.AutoField(primary_key=True, verbose_name="ไอดีการซ่อมเสีย")
    work_location = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='สาขาที่ซ่อม')
    work_machine = models.ForeignKey(BranchMachine, on_delete=models.CASCADE,
                                    verbose_name='เครื่องที่ซ่อม')
    tech_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  limit_choices_to={'user_type': 4},
                                  verbose_name = 'ชื่อช่างที่ซ่อม')
    work_fix = models.ForeignKey(Notification, on_delete=models.CASCADE,
                                 limit_choices_to={'work_status': 2},

                                 verbose_name='สาเหตุ')
    confirm_photo = models.ImageField( verbose_name = 'รูปถ่ายการซ่อม', upload_to='confirm_photo/', max_length=60)
    todo_date = models.DateTimeField(verbose_name = 'วันที่มอบหมายงาน', auto_now_add=True, auto_now=False)
    finish_date = models.DateTimeField(verbose_name = 'วันที่เสร็จงาน', auto_now=True)
    comment = models.CharField(verbose_name='ข้อคิดเห็น', blank=True, null=True, max_length=60, help_text='ถ้ามี')
    price = models.DecimalField(verbose_name='ค่าใช้จ่าย',max_digits=12, decimal_places=2,default=0)
    STATUS_CHOICES = (
        (1, 'กำลังดำเนินการ'),
        (2, 'ซ่อมเรียบร้อย'),
        (3, 'ซ่อมไม่ได้'),
    )
    work_status = models.PositiveSmallIntegerField(verbose_name = 'สถานะของงาน',choices=STATUS_CHOICES,blank=True,null=True,default=1)#confirm by admin
    def __str__(self):
        return 'ชื่อเครื่อง %s สาขา %s %s ' %(self.work_machine.machine_name,self.work_location.branch_name,self.work_fix)
    class Meta:
        verbose_name = 'งานของช่าง'
        verbose_name_plural = 'งานของช่าง'


class MachineMaintained(models.Model):
    maintaine_id = models.AutoField(primary_key=True, verbose_name="ไอดีการซ่อม")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='สาขา')
    tech_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  limit_choices_to={'user_type': 4},
                                  verbose_name = 'ชื่อช่างที่ซ่อม')
    date = models.DateTimeField(verbose_name = 'วันที่มอบหมายงาน',auto_now_add=True,auto_now=False)
    comment = models.CharField(verbose_name='ข้อคิดเห็น', blank=True, null=True, max_length=60, help_text='ถ้ามี')
    WORK_CHOICES = (
        (1, 'งานซ่อมทั่วไป'),
        (2, 'งานซ่อมบำรุง'),

    )
    work = models.PositiveSmallIntegerField(verbose_name = 'ประเภทของงาน',choices=WORK_CHOICES,blank=True,null=True)
    price = models.DecimalField(verbose_name='ค่าใช้จ่าย',max_digits=12, decimal_places=2,default=0)
    STATUS_CHOICES = (
        (1, 'มอบหมายงานแล้ว'),
        (2, 'ซ่อมเรียบร้อย'),
        (3, 'ซ่อมไม่ได้'),
    )
    status = models.PositiveSmallIntegerField(verbose_name = 'สถานะของงาน',choices=STATUS_CHOICES,blank=True,null=True,default=1)
