from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse ,HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView,FormView,FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView)
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import View
from branches.models import Branch,BranchWithdraw
from owners.models import  OwnerBranch
from .forms import BranchForm,BranchUpdateForm,  BranchWithdrawForm, BranchWithdrawUpdateForm
from profits.forms import CreateProfit, UpdateProfit
from profits.models import ProfitMachine
# Create your views here.


#Branch
@login_required(login_url='/users/login/')
def branch_list(request):
    branches = Branch.objects.all().order_by('-branch_id')
    # paginator = Paginator(branches, 20)
    # page = request.GET.get('branches')
    # try:
    #     branch = paginator.page(page)
    # except PageNotAnInteger:
    #     branch = paginator.page(1)
    # except EmptyPage:
    #     branch = paginator.page(paginator.num_pages)
    return render(request, 'branches/manage_branch.html', {'branches': branches})
@login_required(login_url='/users/login/')
def detail_owner(request, pk):
    branch = Branch.objects.filter(branch_id__pk=pk)
    owner = OwnerBranch.objects.filter(branch_branch_id__pk=pk)
    return render(request, 'branches/detail.html', {'branch': branch,'owner':owner})

class BranchDetail(DetailView):
    context_object_name = 'branch'
    model = Branch
    template_name ='branches/detail.html'

@login_required(login_url='/users/login/')
def save_branch_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            # print("form is valid")
            form.save()
            data['form_is_valid'] = True
            branches = Branch.objects.all().order_by('-branch_id')
            data['html_branch_list'] = render_to_string('branches/includes/partial_branch_list.html', {
                'branches': branches
            })
            return HttpResponseRedirect('/branches/branches/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST ,request.FILES)
        form.save()
    else:
        form = BranchForm()
    return save_branch_form(request, form, 'branches/includes/partial_branch_create.html')

@login_required(login_url='/users/login/')
def branch_update(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchUpdateForm(request.POST, instance=branch)
        # return HttpResponseRedirect('/branches/branches/')
    else:
        form = BranchUpdateForm(instance=branch)
    return save_branch_form(request, form, 'branches/includes/partial_branch_update.html')

@login_required(login_url='/users/login/')
def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    data = dict()
    if request.method == 'POST':
        branch.delete()
        data['form_is_valid'] = True
        branches = Branch.objects.all().order_by('-branch_id')
        data['html_branch_list'] = render_to_string('branches/includes/partial_branch_list.html', {
            'branches': branches
        })
        return HttpResponseRedirect('/branches/branches/')
    else:
        context = {'branch': branch}
        data['html_form'] = render_to_string('branches/includes/partial_branch_delete.html', context, request=request)
    return JsonResponse(data)


#Monthly MonthlyMoney,BranchWithdraw MonthlyMoneyForm, MonthlyMoneyUpdateForm, BranchWithdrawForm, BranchWithdrawUpdateForm
# def monthly_list(request):
#     months = MonthlyMoney.objects.all()
#     return render(request, 'branches/manage_monthly.html', {'months': months})
#
# def save_monthly_form(request, form, template_name):
#     data = dict()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             months = MonthlyMoney.objects.all()
#             data['html_monthly_list'] = render_to_string('branches/monthly/partial_monthly_list.html', {
#                 'months': months
#             })
#         else:
#             data['form_is_valid'] = False
#     context = {'form': form}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)
#
#
# def monthly_create(request):
#     if request.method == 'POST':
#         form = MonthlyMoneyForm(request.POST)
#     else:
#         form = MonthlyMoneyForm()
#     return save_monthly_form(request, form, 'branches/monthly/partial_monthly_create.html')
#
#
# def monthly_update(request, pk):
#     month = get_object_or_404(MonthlyMoney, pk=pk)
#     if request.method == 'POST':
#         form = MonthlyMoneyUpdateForm(request.POST, instance=month)
#     else:
#         form = MonthlyMoneyUpdateForm(instance=month)
#     return save_monthly_form(request, form, 'branches/monthly/partial_monthly_update.html')
#
#
# def monthly_delete(request, pk):
#     month = get_object_or_404(MonthlyMoney, pk=pk)
#     data = dict()
#     if request.method == 'POST':
#         month.delete()
#         data['form_is_valid'] = True
#         months = MonthlyMoney.objects.all()
#         data['html_monthly_list'] = render_to_string('branches/monthly/partial_monthly_list.html', {
#             'months': months
#         })
#     else:
#         context = {'month': month}
#         data['html_form'] = render_to_string('branches/monthly/partial_monthly_delete.html', context, request=request)
#     return JsonResponse(data)




#Withdraw BranchWithdraw BranchWithdrawForm, BranchWithdrawUpdateForm
@login_required(login_url='/users/login/')
def withdraw_list(request):
    withdraws = ProfitMachine.objects.all().order_by('-id')
    #sumwithdraw = BranchWithdraw.objects.all().aggregate(Sum('branch_check_money'))
    # paginator = Paginator(withdraws, 10)
    # page = request.GET.get('withdraws')
    # try:
    #     withdraws = paginator.page(page)
    # except PageNotAnInteger:
    #     withdraws = paginator.page(1)
    # except EmptyPage:
    #     withdraws = paginator.page(paginator.num_pages)
    return render(request, 'branches/manage_withdraw.html', {'withdraws': withdraws})



class WithdrawDetail(LoginRequiredMixin,DetailView):
    model = BranchWithdraw
    template_name = 'branches/manage_withdraw_detail.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['withdraws'] = BranchWithdraw.objects.filter(user_save_id__pk=self.kwargs.get('pk'))
        # find sum
        # current_money = OwnerBranch.objects.filter(machine_location__pk=self.kwargs.get('pk')).aggregate(Sum('current_money'))
        # context['current_money'] = current_money
        return context
@login_required(login_url='/users/login/')
def save_withdraw_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            withdraws = ProfitMachine.objects.all().order_by('-id')
            data['html_withdraw_list'] = render_to_string('branches/withdraw/partial_withdraw_list.html', {
                'withdraws': withdraws
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class CreateWithdraw(LoginRequiredMixin,CreateView):
    model = BranchWithdraw
    fields =['branch','branch_check_money',]
    template_name ='branches/withdraw/wd_create.html'
    success_url = reverse_lazy('users:dashboard')

@login_required(login_url='/users/login/')
def withdraw_create(request):
    if request.method == 'POST':
        form = CreateProfit(request.POST)
    else:
        form = CreateProfit()
    return save_withdraw_form(request, form, 'branches/withdraw/partial_withdraw_create.html')

@login_required(login_url='/users/login/')
def withdraw_update(request, pk):
    withdraw = get_object_or_404(ProfitMachine, pk=pk)
    if request.method == 'POST':
        form = UpdateProfit(request.POST, instance=withdraw)
    else:
        form = UpdateProfit(instance=withdraw)
    return save_withdraw_form(request, form, 'branches/withdraw/partial_withdraw_update.html')

@login_required(login_url='/users/login/')
def withdraw_delete(request, pk):
    withdraw = get_object_or_404(ProfitMachine, pk=pk)
    data = dict()
    if request.method == 'POST':
        withdraw.delete()
        data['form_is_valid'] = True
        withdraws = ProfitMachine.objects.all().order_by('-id')
        data['html_withdraw_list'] = render_to_string('branches/withdraw/partial_withdraw_list.html', {
            'withdraws': withdraws
        })
    else:
        context = {'withdraw': withdraw}
        data['html_form'] = render_to_string('branches/withdraw/partial_withdraw_delete.html', context, request=request)
    return JsonResponse(data)
