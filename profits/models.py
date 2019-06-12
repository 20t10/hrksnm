from django.db import models
from branches.models import Branch
from machines.models import BranchMachine

class ProfitMachine(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, null=True,verbose_name = 'สาขา')
    machine = models.ForeignKey(BranchMachine, on_delete=models.DO_NOTHING, null=True,verbose_name = 'เครื่อง')
    check_date = models.DateTimeField(verbose_name = 'เช็ควันที่',auto_now=True)
    check_update = models.DateTimeField(verbose_name = 'วันที่แก้ไข',auto_now_add=True)
    check_money = models.DecimalField(verbose_name = 'จำนวนเงิน',max_digits=10, decimal_places=2)
    fix_money = models.DecimalField(verbose_name = 'ค่าซ่อม',max_digits=10, decimal_places=2)
    
    
    @property
    def profit_last(self):

    	return self.check_money - self.fix_money
        
    	# {{ obj.profit }}
    
    def __str__(self):
        return str(self.check_date)


        