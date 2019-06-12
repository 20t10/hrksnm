from rest_framework import serializers
from .models import Notification
from branches.models import BranchWithdraw
class NotificationModelSerializers(serializers.ModelSerializer):
     class Meta:
         model = Notification
         fields = [
             'work_status',

         ]
class BranchWithdrawModelSerializers(serializers.ModelSerializer):
     class Meta:
         model = BranchWithdraw
         fields = [
             'branch','branch_check_money',
               

         ]