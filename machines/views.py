from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models.functions import TruncMonth, TruncYear, TruncDay, TruncWeek
from datetime import date, datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from itertools import chain
from django.contrib.auth.decorators import login_required
from bootstrap_datepicker_plus import DateTimePickerInput
#tech
from technicians.models import Notification
from technicians.forms import BrokenUpdateForm
from .models import BranchMachine, MachineLog, MachineReal
from .forms import MachineFormCreate, MachineFormUpdate,MachineLogCreate, MachineLogUpdate,MachineRealCreate, MachineRealUpdate
# serialize
from rest_framework import generics
from .serializers import BranchMachineModelSerializer,MachineLogSerializer,MachineRealSerializer


#api
class MachineListAPIView(generics.ListAPIView):
     serializer_class = BranchMachineModelSerializer
     def get_queryset(self):
          return BranchMachine.objects.filter(machine_location__pk=self.kwargs.get('pk'))

class MachineListBranchAPIView(generics.ListAPIView):
     serializer_class = BranchMachineModelSerializer
     def get_queryset(self):
          return BranchMachine.objects.filter(machine_location__pk=self.kwargs.get('pk'))


class MachineLogAPIView(generics.ListAPIView):
    serializer_class = MachineLogSerializer
    def get_queryset(self):
        return MachineLog.objects.filter(log_branch__pk=self.kwargs.get('pk'))

class MachineRealAPIView(generics.ListAPIView):
    serializer_class = MachineRealSerializer
    def get_queryset(self):
        return MachineReal.objects.filter(machine__pk=self.kwargs.get('pk'))
#show?
@login_required(login_url='/users/login/')
def machine_list_module(request):
    machines = BranchMachine.objects.all().order_by('-id')
    # paginator = Paginator(machines, 20)
    # page = request.GET.get('machines')
    # try:
    #     machine = paginator.page(page)
    # except PageNotAnInteger:
    #     machine = paginator.page(1)
    # except EmptyPage:
    #     machine = paginator.page(paginator.num_pages)
    return render(request, 'owners/machines_income/machine_list.html', {'machines': machines})
@login_required(login_url='/users/login/')
def machine_detail_module(request, pk):
    machine = get_object_or_404(BranchMachine, pk=pk)
    return render(request, 'owners/machines_income/machine_detail.html', {'machine': machine})


###
@login_required(login_url='/users/login/')
def machine_list(request):
    machines = BranchMachine.objects.all().order_by('-id')
    paginator = Paginator(machines, 20)
    page = request.GET.get('machines')
    try:
        machine = paginator.page(page)
    except PageNotAnInteger:
        machine = paginator.page(1)
    except EmptyPage:
        machine = paginator.page(paginator.num_pages)
    return render(request, 'machines/manage_machine.html', {'machines': machines})
@login_required(login_url='/users/login/')
def machine_income(request):
    search_term = ''
    mf = BranchMachine.objects.all().order_by('machine_repair', '-machine_repair')
    paginator = Paginator(mf, 2)
    page = request.GET.get('mf')
    try:
        mf = paginator.page(page)
    except PageNotAnInteger:
        mf = paginator.page(1)
    except EmptyPage:
        mf = paginator.page(paginator.num_pages)
    if 'search' in request.GET:
        search_term = request.GET['search']
        mf = BranchMachine.objects.filter(
            Q(machine_repair__icontains=search_term) |
           # Q(is_broken__icontains=search_term) |
            Q(machine_status__icontains=search_term)
        )

    machines = BranchMachine.objects.all()
    # mf = BranchMachine.objects.all().order_by('machine_repair', '-machine_repair')
    return render(request, 'machines/detail_money.html', {'machines': machines, 'mf':mf})
@login_required(login_url='/users/login/')
def machine_detail_coin(request):
    machines = BranchMachine.objects.all()
    return render_to_response(request, 'machines/machine_detail_coin.html', {'machines': machines})


@login_required(login_url='/users/login/')
def save_machine_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            machines = BranchMachine.objects.all().order_by('-id')
            data['html_machine_list'] = render_to_string('machines/includes/partial_machine_list.html', {
                'machines': machines
            })

        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def machine_create(request):
    if request.method == 'POST':
        form = MachineFormCreate(request.POST)
    else:
        form = MachineFormCreate()
    return save_machine_form(request, form, 'machines/includes/partial_machine_create.html')

@login_required(login_url='/users/login/')
def machine_update(request, pk):
    machine = get_object_or_404(BranchMachine, pk=pk)
    if request.method == 'POST':
        form = MachineFormUpdate(request.POST, instance=machine)
    else:
        form = MachineFormUpdate(instance=machine)
    return save_machine_form(request, form, 'machines/includes/partial_machine_update.html')

@login_required(login_url='/users/login/')
def machine_delete(request, pk):
    machine = get_object_or_404(BranchMachine, pk=pk)
    data = dict()
    if request.method == 'POST':
        machine.delete()
        data['form_is_valid'] = True
        machines = BranchMachine.objects.all().order_by('-id')
        data['html_machine_list'] = render_to_string('machines/includes/partial_machine_list.html', {
            'machines': machines
        })
    else:
        context = {'machine': machine}
        data['html_form'] = render_to_string('machines/includes/partial_machine_delete.html', context, request=request)
    return JsonResponse(data)
@login_required(login_url='/users/login/')
def fix_list(request):
    machines = BranchMachine.objects.all().order_by('-id')
    notifications = Notification.objects.all().order_by('-id')
    return render(request, 'machines/fix_machine/fix_manage.html', {'machines': machines,'notifications':notifications})

#log
@login_required(login_url='/users/login/')
def log_list(request):
    logs = MachineLog.objects.all()
    return render(request, 'machines/manage_log.html', {'logs': logs})
@login_required(login_url='/users/login/')
def save_log_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            logs = MachineLog.objects.all()
            data['html_log_list'] = render_to_string('machines/log/partial_log_list.html', {
                'logs': logs
            })

        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def log_create(request):
    if request.method == 'POST':
        form = MachineLogCreate(request.POST)
    else:
        form = MachineLogCreate()
    return save_log_form(request, form, 'machines/log/partial_log_create.html')

@login_required(login_url='/users/login/')
def log_update(request, pk):
    log = get_object_or_404(MachineLog, pk=pk)
    if request.method == 'POST':
        form = MachineLogUpdate(request.POST, instance=log)
    else:
        form = MachineLogUpdate(instance=log)
    return save_machine_form(request, form, 'machines/log/partial_log_update.html')

@login_required(login_url='/users/login/')
def log_delete(request, pk):
    log = get_object_or_404(MachineLog, pk=pk)
    data = dict()
    if request.method == 'POST':
        log.delete()
        data['form_is_valid'] = True
        logs = MachineLog.objects.all()
        data['html_machine_list'] = render_to_string('machines/log/partial_log_list.html', {
            'logs': logs
        })
    else:
        context = {'log': log}
        data['html_form'] = render_to_string('machines/log/partial_log_delete.html', context, request=request)
    return JsonResponse(data)


#real
@login_required(login_url='/users/login/')
def real_list(request):
    reals = MachineReal.objects.all()
    return render(request, 'machines/manage_machine.html', {'reals': reals})
@login_required(login_url='/users/login/')
def save_real_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            reals = BranchMachine.objects.all()
            data['html_machine_list'] = render_to_string('machines/real/partial_real_list.html', {
                'reals': reals
            })

        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def real_create(request):
    if request.method == 'POST':
        form = MachineRealCreate(request.POST)
    else:
        form = MachineRealCreate()
    return save_machine_form(request, form, 'machines/real/partial_real_create.html')

@login_required(login_url='/users/login/')
def real_update(request, pk):
    real = get_object_or_404(MachineReal, pk=pk)
    if request.method == 'POST':
        form = MachineRealUpdate(request.POST, instance=real)
    else:
        form = MachineRealUpdate(instance=real)
    return save_machine_form(request, form, 'machines/real/partial_real_update.html')

@login_required(login_url='/users/login/')
def real_delete(request, pk):
    real = get_object_or_404(MachineReal, pk=pk)
    data = dict()
    if request.method == 'POST':
        real.delete()
        data['form_is_valid'] = True
        reals = MachineReal.objects.all()
        data['html_machine_list'] = render_to_string('machines/real/partial_real_list.html', {
            'reals': reals
        })
    else:
        context = {'real': real}
        data['html_form'] = render_to_string('machines/includes/partial_real_delete.html', context, request=request)
    return JsonResponse(data)
