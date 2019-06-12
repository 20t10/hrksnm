from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
# icon brand ยินดี about
class managesite(models.Model):
    icon = models.ImageField(verbose_name = 'ไอคอนเว็บไซต์',upload_to='site_manage/',max_length=60,help_text='ชื่อไฟล์ไม่เกิน60ตัวอักษร')
    brand = models.CharField(verbose_name='ชื่อไซต์',max_length=20,help_text='ไม่เกิน20ตัวอักษร')
    welcome = models.TextField(verbose_name='ข้อความต้อนรับ')
    about = models.CharField(verbose_name='เกี่ยวกับเรา',max_length=100,help_text='ไม่เกิน100ตัวอักษร')
    service = models.TextField(verbose_name='การให้บริการ')
    contact = models.CharField(verbose_name='ติดต่อเรา', max_length=100,help_text='ไม่เกิน100ตัวอักษร')
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=True, null=True)
    class Meta:
        db_table = 'index_site'

class serviceimg(models.Model):
    service_id = models.AutoField(primary_key=True, verbose_name="ไอดีรูป")
    img = models.ImageField(verbose_name='รูปภาพ', upload_to='site_manage/service', max_length=60,help_text='ชื่อไฟล์ไม่เกิน60ตัวอักษร')
    detail = models.CharField(verbose_name='คำอธิบาย',max_length=60,help_text='ไม่เกิน60ตัวอักษร')
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=True, null=True)
    class Meta:
        db_table = 'service_img'

class faqsite(models.Model):
    faq_id = models.AutoField(primary_key=True, verbose_name="ไอดีคำถาม/ตอบ")
    question = models.CharField(verbose_name='คำถาม', max_length=100)
    answered = models.CharField(verbose_name='คำตอบ', max_length=100)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=True, null=True)
