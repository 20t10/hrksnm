from rest_framework import serializers
from .models import BranchMachine, MachineLog, MachineReal

class BranchMachineModelSerializer(serializers.ModelSerializer):
     class Meta:
         model = BranchMachine
         fields = [
             'machine_url',
             'machine_name',
             'machine_location',
             'machine_ip',
             'machine_status',
             'machine_repair',
             'next_fix',
             'is_broken',
         ]


class MachineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLog
        fields = [
            'log_id',
            'log_thb',
            'log_module',
            'log_branch',
            'log_date',
            'log_time',

        ]


class MachineRealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineReal
        fields = [
            'real_id',
            'machine',
            'real_thb',
            'real_date',
            'real_time',

        ]