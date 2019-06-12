from django.shortcuts import render
from django.views.generic import ListView
from .models import ProfitMachine


class ProfitsListView(ListView):
	model = ProfitMachine
	template_name = 'machines/machine_profit.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["profit"] = ProfitMachine.objects.all()
		return context
	