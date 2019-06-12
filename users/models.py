from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# owner and tech
class User(AbstractUser):

  USER_TYPE_CHOICES = (
  (1, 'แอดมิน'),
  (2, 'พนักงาน'),
  (3, 'เจ้าของกิจการ'),
  (4, 'ช่างซ่อม'),

  )
  user_id = models.AutoField(primary_key=True, verbose_name="ไอดีผู้ใช้")
  username = models.CharField(unique=True,verbose_name='ชื่อผู้ใช้',max_length=20,help_text='ไม่เกิน20ตัวอักษร เป็นตัวอักษรภาษาอังกฤษ ผสมกับตัวเลขได้',)
  password = models.CharField(verbose_name='รหัสผ่าน',max_length=100,help_text='รหัสผ่านขั้นต่ำ8ตัวอักษร เป็นตัวอักษรภาษาอังกฤษ ผสมกับตัวเลขได้',)
  organization = models.CharField(verbose_name='ชื่อ องค์กร',max_length=30,help_text='ไม่เกิน30ตัวอักษร', blank=True, null=True)
  email = models.EmailField(unique=True,max_length=50,help_text='ตัวอย่างเช่น user@email.com')
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,verbose_name='สถานะผู้ใช้งาน', blank=True, null=True)

  def __str__(self):
    return '%s %s %s %s' %(self.username, self.first_name, self.last_name, self.organization)
