from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse ,HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView,FormView,FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from branches.models import BranchWithdraw
from technicians.models import TodoList,Notification,MachineMaintained
from machines.models import BranchMachine
from .forms import TodoCreateForm, ConfirmTodo,TechSend,SendNotiForm,BrokenUpdateForm,FixUpdateForm,CreateNotiForm,Maintained,MaintainedConfirm, TechMaintained

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
class ChartFixedBranchData(APIView):
    authentication_classes = []
    permission_classes = (IsAuthenticated|ReadOnly,)
    def get(self, request, format=None):
        
        fixed_count = TodoList.objects.values('work_location__branch_name').annotate(wcount=Count('work_location')) #branch distinct 3
       
        
       
        default_items = [fixed_count]
        data = {
                 
                "default": default_items,
        }
        return Response(data)
#branch money
class ChartMoneyBranchData(APIView):
    authentication_classes = []
    permission_classes = (IsAuthenticated|ReadOnly,)
    def get(self, request, format=None):
        branch_list = BranchWithdraw.objects.values('branch__branch_name').distinct()
        branch_count = BranchWithdraw.objects.values('branch__branch_name').annotate(bcount=Count('branch')) #branch distinct 3
        labels = ["branch_list"]
      
        #print(branch_list.distinct())


        default_items = [branch_count]
        data = {
                 
                "default": default_items,
        }
        return Response(data)

class ChartNotiData(APIView):
    authentication_classes = []
    permission_classes = (IsAuthenticated|ReadOnly,)
    def get(self, request, format=None):
        finish = Notification.objects.filter(work_status=3).count()
        fail = Notification.objects.filter(work_status=4).count()
        #detail = Notification.objects.filter(Q(work_status=3) | Q(work_status=4))
        labels = ["ซ่อมเรียบร้อย", "ซ่อมไม่ได้"]
        #print(detail)
        default_items = [finish, fail]
        data = {
                 "labels": labels,
                "default": default_items,
        }
        return Response(data)
class ChartView(ListView):
    model = Notification
    template_name = 'teches/count_fix.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finnish'] = Notification.objects.filter(work_status=3) .aggregate(Count('work_status'))
        context['unfinnish'] = Notification.objects.filter(work_status=4) .aggregate(Count('work_status'))
        
        # find sum
        # countnoti = Notification.objects.filter(machine_location__pk=self.kwargs.get('pk')).aggregate(Sum('current_money'))
        # context['countnoti'] = countnoti
        # context['countnoti'] = current_money
        return context
class ChartMoneyView(ListView):
    model = BranchWithdraw
    template_name = 'teches/chartmoney.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['withdraws'] = BranchWithdraw.objects.all()        
        #print(context)
        # find sum
        # countnoti = Notification.objects.filter(machine_location__pk=self.kwargs.get('pk')).aggregate(Sum('current_money'))
        # context['countnoti'] = countnoti  .aggregate(Count('work_status'))
        # context['countnoti'] = current_money
        return context    
class ChartFixedView(ListView):
    model = TodoList
    template_name = 'teches/chartfixed.html'   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = TodoList.objects.filter(work_status=2)        
        #print(context)
        # find sum
        # countnoti = Notification.objects.filter(machine_location__pk=self.kwargs.get('pk')).aggregate(Sum('current_money'))
        # context['countnoti'] = countnoti  .aggregate(Count('work_status'))
        # context['countnoti'] = current_money
        return context

@login_required(login_url='/users/login/')
def tb_noti(request, *args, **kwargs):
    finish = Notification.objects.filter(work_status=3).count()
    fail = Notification.objects.filter(work_status=4).count()
    return render(request, 'teches/tb_noti.html', {'finish':finish, 'fail':fail})

@login_required(login_url='/users/login/')
def ShowBroken(request):
    stop = Notification.objects.filter(fix_description_choices=1).count()
    coin = Notification.objects.filter(fix_description_choices=2).count()
    hang = Notification.objects.filter(fix_description_choices=3).count()
    clean = Notification.objects.filter(fix_description_choices=4).count()

    print(stop, coin, hang, clean)
    # labels = ["เครื่องค้าง", "เหรียญเต็ม", "เครื่องไม่ทำงาน", "ล้างเครื่อง"]
    # default_items = [stop,coin,hang,clean]
    # data = {
    #     "labels":labels ,
    #     "default": default_items,
        # 'เหรียญเต็ม':coin ,
        # 'เครื่องไม่ทำงาน':hang ,
        # 'ล้างเครื่อง':clean ,
    # }
    #,'coin':coin,'hank':hank,'clean':clean
    return render(request,'teches/cf_normal.html',{'stop':stop,'coin':coin,'hang':hang,'clean':clean})
    # return JsonResponse(data)


#todo
@login_required(login_url='/users/login/')
def todo_list(request):
    todos = TodoList.objects.filter(work_status=1).order_by('-todo_id')
    nt = Notification.objects.all().order_by('-noti_id')
    # paginator = Paginator(todos, 20)
    # page = request.GET.get('todos')
    # try:
    #     todo = paginator.page(page)
    # except PageNotAnInteger:
    #     todo = paginator.page(1)
    # except EmptyPage:
    #     todo = paginator.page(paginator.num_pages)
    return render(request, 'teches/manage_todo.html', {'todos': todos,'nt':nt})

@login_required(login_url='/users/login/')
def save_todo_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            # print("form is valid")
            form.save()
            data['form_is_valid'] = True
            todos = TodoList.objects.all().order_by('-todo_id')
            data['html_todo_list'] = render_to_string('teches/includes/partial_todo_list.html', {
                'todos': todos
            })
            return HttpResponseRedirect('/teches/todo/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def todo_create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST ,request.FILES)
        form.save()
    else:
        form = TodoCreateForm()
    return save_todo_form(request, form, 'teches/includes/partial_todo_create.html')

@login_required(login_url='/users/login/')
def todo_update(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        form = ConfirmTodo(request.POST,instance=todo)
        # return HttpResponseRedirect('/teches/todo/')
    else:
        form = ConfirmTodo(instance=todo)
        # print(form.errors)
        # print(form.non_field_errors)
        # twiml = '<Response><Message>No</Message></Response>'
        # print(twiml)
    return save_todo_form(request, form, 'teches/includes/partial_todo_update.html')
@login_required(login_url='/users/login/')
def todo_delete(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    data = dict()
    if request.method == 'POST':
        todo.delete()
        data['form_is_valid'] = True
        todos = TodoList.objects.all().order_by('-todo_id')
        data['html_todo_list'] = render_to_string('teches/includes/partial_todo_list.html', {
            'todos': todos
        })
        return HttpResponseRedirect('/teches/todo/')
    else:
        context = {'todo': todo}
        data['html_form'] = render_to_string('teches/includes/partial_todo_delete.html', context, request=request)
    return JsonResponse(data)

#tech actions
@login_required(login_url='/users/login/')
def tech_todo(request):
    todos = TodoList.objects.filter(tech_name=request.user, work_status=1).order_by('-todo_id')

    return render(request, 'teches/tech_todo.html', {'todos': todos})
@login_required(login_url='/users/login/')
def log_todo(request):

    hiswork = TodoList.objects.filter(tech_name=request.user)

    return render(request, 'teches/tech_todo_log.html', {'hiswork':hiswork})

@login_required(login_url='/users/login/')
def alllog_todo(request):
    all = TodoList.objects.all().order_by('-todo_id')
    hiswork = TodoList.objects.filter(work_status=2).order_by('-todo_id')
    failwork = TodoList.objects.filter(work_status=3).order_by('-todo_id')
    return render(request, 'teches/all_todo_log.html', {'all':all,'hiswork':hiswork,'failwork':failwork})

@login_required(login_url='/users/login/')
def save_work_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            # print("form is valid")
            form.save()
            data['form_is_valid'] = True
            todos = TodoList.objects.all().order_by('-todo_id')
            data['html_todo_list'] = render_to_string('teches/tech/ttd_list.html', {
                'todos': todos
            })
            return HttpResponseRedirect('/teches/tech/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def work_create(request):
    if request.method == 'POST':
        form = TechSend(request.POST ,request.FILES)
        form.save()
    else:
        form = TechSend()
    return save_todo_form(request, form, 'teches/tech/ttd_send.html')

@login_required(login_url='/users/login/')
def work_update(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        form = TechSend(request.POST,request.FILES, instance=todo)
        # return HttpResponseRedirect('/teches/tech/')
    else:
        form = TechSend(instance=todo)
    return save_work_form(request, form, 'teches/tech/ttd_send.html')

@login_required(login_url='/users/login/')
def work_delete(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    data = dict()
    if request.method == 'POST':
        todo.delete()
        data['form_is_valid'] = True
        todos = TodoList.objects.all().order_by('-todo_id')
        data['html_todo_list'] = render_to_string('teches/tech/ttd_list.html', {
            'todos': todos
        })
        return HttpResponseRedirect('/teches/tech/')
    else:
        context = {'todo': todo}
        data['html_form'] = render_to_string('teches/tech/ttd_delete.html', context, request=request)
    return JsonResponse(data)

# send notifications

@login_required(login_url='/users/login/')
def work_create(request):
    if request.method == 'POST':
        form = TechSend(request.POST ,request.FILES)
        form.save()
    else:
        form = TechSend()
    return save_todo_form(request, form, 'teches/tech/ttd_send.html')

def notification_send(request):
    if request.method == 'POST':
        form = SendNotiForm(request.POST)
        form.save()
    else:
        form = SendNotiForm()
    return render(request, 'teches/noti/send_noti.html',{'form':form})

class SendNotification(CreateView):
    model = Notification
    form_class = SendNotiForm
    #fields = ['user_send','from_branch','machine','fix_description_choices','fix_description_extra',]
    template_name = 'teches/noti/form_send.html'
    success_url = reverse_lazy('teches:fix_send_form')


def load_machines(request):
    branch_id = request.GET.get('branch')
    machines = BranchMachine.objects.filter(machine_location_id=branch_id)
    #print(machines)
    return render(request, 'teches/noti/machine_dropdown_list_options.html', {'machines': machines})

# emp change status
@login_required(login_url='/users/login/')
def noti_list(request):
    notis = Notification.objects.all().order_by('-noti_id')

    # paginator = Paginator(notis, 20)
    # page = request.GET.get('notis')
    # try:
    #     noti = paginator.page(page)
    # except PageNotAnInteger:
    #     noti = paginator.page(1)
    # except EmptyPage:
    #     noti = paginator.page(paginator.num_pages)
    return render(request, 'teches/manage_broken.html', {'notis': notis})


@login_required(login_url='/users/login/')
def save_noti_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            notis = Notification.objects.all().order_by('-noti_id')
            data['html_noti_list'] = render_to_string('teches/fix_update/partial_noti_list.html', {
                'notis': notis
            })
            # return HttpResponseRedirect('/teches/noti_list/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def noti_create(request):
    if request.method == 'POST':
        form = CreateNotiForm(request.POST)
        form.save()
        # return HttpResponseRedirect('/teches/noti_list/')
    else:
        form = CreateNotiForm()
    return save_noti_form(request, form, 'teches/fix_update/partial_noti_create.html')

@login_required(login_url='/users/login/')
def noti_update(request, pk):
    noti = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = FixUpdateForm(request.POST, instance=noti)
        # return HttpResponseRedirect('/teches/noti_list/')
    else:
        form = FixUpdateForm(instance=noti)
    return save_noti_form(request, form, 'teches/fix_update/partial_noti_update.html')

@login_required(login_url='/users/login/')
def noti_delete(request, pk):
    noti = get_object_or_404(Notification, pk=pk)
    data = dict()
    if request.method == 'POST':
        noti.delete()
        data['form_is_valid'] = True
        notis = Notification.objects.all().order_by('-noti_id')
        data['html_noti_list'] = render_to_string('teches/fix_update/partial_noti_list.html', {
            'notis': notis
        })
        # return HttpResponseRedirect('/teches/noti_list/')
    else:
        context = {'noti': noti}
        data['html_form'] = render_to_string('teches/fix_update/partial_noti_delete.html', context, request=request)
    return JsonResponse(data)



# MAINTAINED----------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/login/')
def maintaine_list(request):
    maintaines = MachineMaintained.objects.all().order_by('-maintaine_id')

    # paginator = Paginator(maintaines, 20)
    # page = request.GET.get('maintaines')
    # try:
    #     maintaine = paginator.page(page)
    # except PageNotAnInteger:
    #     maintaine = paginator.page(1)
    # except EmptyPage:
    #     maintaine = paginator.page(paginator.num_pages)
    return render(request, 'teches/manage_maintaine.html', {'maintaines':maintaines})

@login_required(login_url='/users/login/')
def maintaine_log(request):
    maintaines_finish = MachineMaintained.objects.filter( work=1).order_by('-maintaine_id')
    # paginator = Paginator(maintaines_finish, 20)
    # page = request.GET.get('maintaines_finish')
    # try:
    #     maintaines_finish = paginator.page(page)
    # except PageNotAnInteger:
    #     maintaines_finish = paginator.page(1)
    # except EmptyPage:
    #     maintaines_finish = paginator.page(paginator.num_pages)

    maintaines_fail = MachineMaintained.objects.filter(work=2).order_by('-maintaine_id')
    # paginator = Paginator(maintaines_fail, 20)
    # page = request.GET.get('maintaines_fail')
    # try:
    #     maintaines_fail = paginator.page(page)
    # except PageNotAnInteger:
    #     maintaines_fail = paginator.page(1)
    # except EmptyPage:
    #     maintaines_fail = paginator.page(paginator.num_pages)

    return render(request, 'teches/maintained_log.html', {'maintaines_finish':maintaines_finish,'maintaines_fail':maintaines_fail})
@login_required(login_url='/users/login/')
def tech_maintaine_log(request):
    maintaines_finish = MachineMaintained.objects.filter(tech_name=request.user).order_by('-maintaine_id')
    print(maintaines_finish)
    maintaines_fail = MachineMaintained.objects.filter(work=2).order_by('-maintaine_id')
    return render(request, 'teches/tech_todo_log_maintain.html', {'maintaines_finish':maintaines_finish,'maintaines_fail':maintaines_fail})

@login_required(login_url='/users/login/')
def save_maintaine_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            maintaines = MachineMaintained.objects.all().order_by('-maintaine_id')
            data['html_maintaine_list'] = render_to_string('teches/maintained/partial_maintaine_list.html', {
                'maintaines': maintaines
            })
            return HttpResponseRedirect('/teches/maintaine/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def maintaine_create(request):
    if request.method == 'POST':
        form = Maintained(request.POST)
        form.save()
    else:
        form = Maintained()
    return save_maintaine_form(request, form, 'teches/maintained/partial_maintaine_create.html')

@login_required(login_url='/users/login/')
def maintaine_update(request, pk):
    maintaine = get_object_or_404(MachineMaintained, pk=pk)
    if request.method == 'POST':
        form = MaintainedConfirm(request.POST, instance=maintaine)
    else:
        form = MaintainedConfirm(instance=maintaine)
    return save_maintaine_form(request, form, 'teches/maintained/partial_maintaine_update.html')

############################################################################################################
@login_required(login_url='/users/login/')
def save_techmaintaine_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            maintaines = MachineMaintained.objects.filter(tech_name=request.user, status=1).order_by('-maintaine_id')
            data['html_maintaine_list'] = render_to_string('teches/maintained/partial_techmaintaine_list.html', {
                'maintaines': maintaines
            })
            return HttpResponseRedirect('/teches/tech_list/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
@login_required(login_url='/users/login/')
def tech_maintaine_list(request):
    maintaines = MachineMaintained.objects.filter(tech_name=request.user, status=1).order_by('-maintaine_id')
    return render(request, 'teches/tech_maintaine.html', {'maintaines':maintaines})

@login_required(login_url='/users/login/')
def maintaine_tech(request, pk):
    maintaine = get_object_or_404(MachineMaintained, pk=pk)
    if request.method == 'POST':
        form = TechMaintained(request.POST, instance=maintaine)
    else:
        form = TechMaintained(instance=maintaine)
    return save_techmaintaine_form(request, form, 'teches/maintained/partial_techmaintaine_update.html')
############################################################################################################
@login_required(login_url='/users/login/')
def maintaine_delete(request, pk):
    maintaine = get_object_or_404(MachineMaintained, pk=pk)
    data = dict()
    if request.method == 'POST':
        maintaine.delete()
        data['form_is_valid'] = True
        maintaines = MachineMaintained.objects.all().order_by('-maintaine_id')
        data['html_maintaine_list'] = render_to_string('teches/maintained/partial_maintaine_list.html', {
            'maintaines': maintaines
        })
        return HttpResponseRedirect('/teches/maintaine/')
    else:
        context = {'maintaine': maintaine}
        data['html_form'] = render_to_string('teches/maintained/partial_maintaine_delete.html', context, request=request)
    return JsonResponse(data)
