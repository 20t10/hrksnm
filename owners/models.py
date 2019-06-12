from django.db import models
from branches.models import Branch
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
# user branches
class OwnerBranch(models.Model):
    owner_id = models.AutoField(primary_key=True, verbose_name="ไอดีเจ้าของสาขา")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
    						limit_choices_to={'user_type': 3},
                             verbose_name='เจ้าของ')
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE,verbose_name='สาขา')

    class Meta:
        db_table = 'owner'
    def __str__(self):
        return self.branch.branch_name
