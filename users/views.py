from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login,logout, get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from users.forms import CreateUser, LoginForm, RegisterForm, UpdateUserForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

#CRUD
from django.views.generic.edit import UpdateView,DeleteView,FormView,FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView)

#
from django.db.models import Q
from itertools import chain
#
from branches.models import Branch
from owners.models import OwnerBranch
from technicians.models import Notification
#
from users.forms import RegisterForm,LoginForm,UpdateUserForm

from django.contrib.auth.models import User

User = get_user_model()

# User main
# class UserListView(LoginRequiredMixin,ListView):
#     model = User
#     template_name = "users/u_main.html"
#     def get_context_data(self, **kwargs):
#        context = {}
#        user_list = User.objects.all()
#        return context

@login_required(login_url='/users/login/')
def user_list(request):
    users = User.objects.all().order_by('-user_id')
    admin = User.objects.filter(is_superuser=True ).order_by('-user_id')
    emp = User.objects.filter(user_type=2).order_by('-user_id')
    owner = User.objects.filter(user_type=3).order_by('-user_id')
    tech = User.objects.filter(user_type=4).order_by('-user_id')
    
    # paginator = Paginator(users, 20)
    # page = request.GET.get('users')
    # try:
    #     user = paginator.page(page)
    # except PageNotAnInteger:
    #     user = paginator.page(1)
    # except EmptyPage:
    #     user = paginator.page(paginator.num_pages)
    return render(request, 'users/manage_user.html', {'users':users,'admin': admin,'emp': emp, 'owner': owner, 'tech': tech})

@login_required(login_url='/users/login/')
def user_list_manage(request):
    users = User.objects.all()
    branches = Branch.objects.all()
    owner = OwnerBranch.objects.filter(user_id=request.user.user_id)



    return render(request, 'users/u_main.html', {'users': users,'branches':branches, 'owner':owner})

@login_required(login_url='/users/login/')
def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            users = User.objects.all().order_by('-user_id')
            data['html_user_list'] = render_to_string('users/includes/partial_user_list.html', {
                'users': users
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def user_create(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
    else:
        form = CreateUser()
    return save_user_form(request, form, 'users/includes/partial_user_create.html')

@login_required(login_url='/users/login/')
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
    else:
        form = UpdateUserForm(instance=user)
    return save_user_form(request, form, 'users/includes/partial_user_update.html')

@login_required(login_url='/users/login/')
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        users = User.objects.all().order_by('-user_id')
        data['html_user_list'] = render_to_string('users/includes/partial_user_list.html', {
            'users': users
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('users/includes/partial_user_delete.html', context, request=request)
    return JsonResponse(data)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        #print(form.cleaned_data)
        ## หลังจากรับค่าแล้วเคลียกล่องรับค่า
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        ##
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            #messages.success(request, "ยินดีต้อนรับเข้าสู่ระบบ")
            return redirect("users:dashboard")# หลังจากล็อกอินเสร็จแล้วไปหน้า
            context['form'] = LoginForm
        else:
            # No backend authenticated the credentials
           # return messages.error(request, "กรุณาตรวจสอบ Username หรือ Password อีกครั้ง")
            print("Error!!! invalid login")
    return render(request, "auth/login.html",context)

#change password
def change_password(request):
    #if request.user == user.is_superuser:

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {
        'form': form
    })
#@login_required
def logout_view(request):

    logout(request)
    return redirect('index')
