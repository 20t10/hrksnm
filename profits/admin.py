from django.contrib import admin
from .models import ProfitMachine

class ProfitMachineAdmin(admin.ModelAdmin):
    model = ProfitMachine
    list_display = ('branch', 'machine',)
    
admin.site.register(ProfitMachine,ProfitMachineAdmin)
