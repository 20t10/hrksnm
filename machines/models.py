from django.db import models
from branches.models import Branch
from datetime import datetime, timedelta
# Create your models here.
class BranchMachine(models.Model):
    
    machine_location = models.ForeignKey(Branch, models.DO_NOTHING,blank=True,null=True,verbose_name='สาขา')#ที่อยู่เครื่อง
    machine_name = models.CharField(verbose_name = 'ชื่อ เครื่อง', max_length=60, help_text='ชื่อสาขา ตามด้วยเลข 01-99')
    machine_repair = models.DateTimeField(verbose_name = 'วันที่ซ่อม',auto_now=False, auto_now_add=True)#นับตั้งแต่วันที่ติดตั้ง
    next_fix = models.DateTimeField(default=datetime.now()+timedelta(days=150),verbose_name = 'การซ่อมครั้งถัดไป')
    #is_broken= models.BooleanField(verbose_name = 'สถานะเครื่องเสีย',default=False)
    def __str__(self):
        return ' %s' %(self.machine_name)
        # return self.machine_name
    class Meta:
        verbose_name = 'เครื่องของสาขา'
        verbose_name_plural = 'เครื่องของสาขา'
 

#save log
class MachineLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_thb = models.DecimalField(max_digits=12, decimal_places=2)
    log_module = models.CharField(max_length=32)
    log_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    log_date = models.DateField(auto_now_add=True)
    log_time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = 'log_module'

#realtime
class MachineReal(models.Model):
    real_id = models.IntegerField(primary_key=True)
    machine = models.ForeignKey(BranchMachine, on_delete=models.CASCADE)
    real_thb = models.DecimalField(max_digits=12, decimal_places=2)
    real_date = models.DateField(auto_now_add=True)
    real_time = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'realtime_module'
