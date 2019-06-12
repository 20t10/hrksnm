from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

#t IMG
from django.utils.safestring import mark_safe

class Branch(models.Model):
    #branch_id = models.IntegerField(primary_key=True,verbose_name= 'รหัสสาขา',max_length=7,unique=True, help_text='รหัสไปรษณีย์ ตามด้วยลำดับสาขา 01-99(ห้ามซ้ำ)')
    branch_id = models.AutoField(primary_key=True,verbose_name= 'IDสาขา')
    branch_img = models.ImageField(verbose_name = 'รูปถ่ายสาขา',upload_to='owner/',max_length=60,help_text='ชื่อไฟล์ไม่เกิน60ตัวอักษร')
    branch_name = models.CharField(verbose_name = 'ชื่อสถานที่',max_length=20,unique=True,help_text='ไม่เกิน20ตัวอักษร')

    branch_address = models.CharField(verbose_name = 'เลขที่อยู่',max_length=50)
    branch_district = models.CharField(verbose_name = 'ตำบล',max_length=30)
    branch_amphoe = models.CharField(verbose_name = 'อำเภอ',max_length=30)
    branch_province = models.CharField(verbose_name = 'จังหวัด',max_length=30)
    branch_zipcode = models.CharField(verbose_name = 'รหัสไปรษณีย์',max_length=5)

    branch_postcode= models.CharField(verbose_name= 'รหัสสาขา',max_length=7,unique=True, help_text='รหัสไปรษณีย์ ตามด้วยลำดับสาขา 01-99(ห้ามซ้ำ)')
    tel_number = models.CharField(verbose_name = 'เบอร์โทรศัพท์1',max_length=10)
    tel_number_two = models.CharField(verbose_name = 'เบอร์โทรศัพท์2',max_length=10,null=True,blank=True)
    tel_number_three = models.CharField(verbose_name = 'เบอร์โทรศัพท์3',max_length=10,null=True,blank=True)

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name = 'จัดการสาขา'
        verbose_name_plural = 'จัดการสาขา'
        db_table = 'branch'



class BranchWithdraw(models.Model):
    withdraw_id = models.AutoField(primary_key=True, verbose_name="ไอดีการบันทึกเงิน")
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, null=True,verbose_name = 'สาขา')
    branch_check_date = models.DateTimeField(verbose_name = 'เช็ควันที่',auto_now=True)
    branch_check_money = models.DecimalField(verbose_name = 'จำนวนเงิน',max_digits=10, decimal_places=2)
    def __str__(self):
        return '%s %s' %(self.branch.branch_name, self.branch_check_money)

    class Meta:
        verbose_name = 'บันทึกการเก็บเงินของสาขา'
        verbose_name_plural = 'บันทึกการเก็บเงินของสาขา'
        db_table = 'branch_money'
