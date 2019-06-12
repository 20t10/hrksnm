from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView,FormView,FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView)
#from src.models  import 1187Log,1187Real
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from branches.models import Branch, BranchWithdraw
from machines.models import BranchMachine
from technicians.models import Notification
from .models import OwnerBranch
from .forms import OwnerForm

from profits.models import ProfitMachine

User = get_user_model()

@login_required(login_url='/users/login/')
def owner_list(request):
    owners = OwnerBranch.objects.all().order_by('-owner_id')

    # paginator = Paginator(owners, 20)
    # page = request.GET.get('owners')
    # try:
    #     owner = paginator.page(page)
    # except PageNotAnInteger:
    #     owner = paginator.page(1)
    # except EmptyPage:
    #     owner = paginator.page(paginator.num_pages)
    return render(request, 'owners/manage_owner.html', {'owners': owners})



#แสดง สาขาที่เป็นเจ้าของ
# show branch in owner
class OwnerShowList(LoginRequiredMixin,ListView):
    model = OwnerBranch
    template_name = 'owners/owner_main_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = OwnerBranch.objects.filter(user_id=self.request.user.user_id)
        return context

class OwnerManage(LoginRequiredMixin,DetailView):
    model = OwnerBranch
    template_name = 'owners/owner_main.html'
    def get_context_data(self, **kwargs):
        #context = {}
        context = super().get_context_data(**kwargs)
        context['owners'] = OwnerBranch.objects.filter(branch_branch_id=self.kwargs.get('pk'))
        # find sum
        # current_money = OwnerBranch.objects.filter(machine_location__pk=self.kwargs.get('pk')).aggregate(Sum('current_money'))
        # context['current_money'] = current_money
        return context

#show list branch
class OwnerBenefitbranch(LoginRequiredMixin,ListView):
    model = BranchWithdraw
    template_name = 'owners/owner_benefit_branch.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branches'] = OwnerBranch.objects.filter(user_id=self.request.user.user_id)
        return context

class OwnerBenefit(LoginRequiredMixin,ListView):
    model = BranchWithdraw
    template_name = 'owners/owner_benefit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['benefit'] = ProfitMachine.objects.filter(branch_id=self.kwargs.get('pk'))
        # find sum
        #context['summoney'] = ProfitMachine.objects.filter(branch_id=self.kwargs.get('pk')).aggregate(Sum('branch_check_money'))
        # context['current_money'] = current_money
        return context

class OwnerNoti(LoginRequiredMixin,ListView):
    model = Notification
    template_name = 'owners/owner_noti.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noti'] = Notification.objects.filter(branch_id__pk=self.kwargs.get('pk'))
        return context
#@xframe_options_exempt

class OwnerBranchList(LoginRequiredMixin,ListView):
    model = BranchMachine
    template_name = 'owners/owner_machine_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = BranchMachine.objects.filter(machine_location__pk=self.kwargs.get('pk'))


        return context
class OwnerBranchDetail(LoginRequiredMixin,TemplateView):
    model = BranchMachine
    template_name = 'owners/owner_machines.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['machines'] = BranchMachine.objects.filter(machine_location__pk=self.kwargs.get('pk'))

        context['branch'] = Branch.objects.filter(pk=self.kwargs.get('pk'))
        return context

@login_required(login_url='/users/login/')
def save_owner_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            owners = OwnerBranch.objects.all().order_by('-owner_id')
            data['html_owner_list'] = render_to_string('owners/includes/partial_owner_list.html', {
                'owners': owners
            })

        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
    else:
        form = OwnerForm()
    return save_owner_form(request, form, 'owners/includes/partial_owner_create.html')

@login_required(login_url='/users/login/')
def owner_update(request, pk):
    owner = get_object_or_404(OwnerBranch, pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
    else:
        form = OwnerForm(instance=owner)
    return save_owner_form(request, form, 'owners/includes/partial_owner_update.html')

@login_required(login_url='/users/login/')
def owner_delete(request, pk):
    owner = get_object_or_404(OwnerBranch, pk=pk)
    data = dict()
    if request.method == 'POST':
        owner.delete()
        data['form_is_valid'] = True
        owners = OwnerBranch.objects.all().order_by('-owner_id')
        data['html_owner_list'] = render_to_string('owners/includes/partial_owner_list.html', {
            'owners': owners
        })
    else:
        context = {'owner': owner}
        data['html_form'] = render_to_string('owners/includes/partial_owner_delete.html', context, request=request)
    return JsonResponse(data)
