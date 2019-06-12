from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy, reverse
from .models import managesite, serviceimg, faqsite
from .forms import SiteForm,SlideForm, FAQForm

#site >index
@login_required(login_url='/users/login/')
def site_list(request):
    sites = managesite.objects.all()
    cs = managesite.objects.all().count
    return render(request, 'sitemanages/manage_site.html', {'sites': sites,'cs':cs})

@login_required(login_url='/users/login/')
def save_site_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            sites = managesite.objects.all()
            data['html_site_list'] = render_to_string('sitemanages/includes/partial_site_list.html', {
                'sites': sites
            })
            return HttpResponseRedirect('/site/site/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def site_create(request):
    if request.method == 'POST':
        form = SiteForm(request.POST,request.FILES)
    else:
        form = SiteForm()
    return save_site_form(request, form, 'sitemanages/includes/partial_site_create.html')

@login_required(login_url='/users/login/')
def site_update(request, pk):
    site = get_object_or_404(managesite, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST,request.FILES, instance=site)
    else:
        form = SiteForm(instance=site)
    return save_site_form(request, form, 'sitemanages/includes/partial_site_update.html')
@login_required(login_url='/users/login/')
def index_update(request, pk, template_name='sitemanages/update_site.html'):
    site= get_object_or_404(managesite, pk=pk)
    form = SiteForm(request.POST or None, instance=site)
    if form.is_valid():
        form.save()
        return redirect('users:dashboard')
    return render(request, template_name, {'form':form})

class SiteUpdateView(LoginRequiredMixin,UpdateView):
    model = managesite
    fields = ['icon', 'brand', 'welcome', 'about', 'service', 'contact', ]
    template_name = 'sitemanages/update_site.html'

@login_required(login_url='/users/login/')
def site_delete(request, pk):
    site = get_object_or_404(managesite, pk=pk)
    data = dict()
    if request.method == 'POST':
        site.delete()
        data['form_is_valid'] = True
        sites = managesite.objects.all()
        data['html_site_list'] = render_to_string('sitemanages/includes/partial_site_list.html', {
            'sites': sites
        })
        return HttpResponseRedirect('/site/site/')
    else:
        context = {'site': site}
        data['html_form'] = render_to_string('sitemanages/includes/partial_site_delete.html', context, request=request)
    return JsonResponse(data)



#index > slide service
@login_required(login_url='/users/login/')
def slide_list(request):
    sls = serviceimg.objects.all().order_by('-service_id')
    return render(request, 'sitemanages/manage_slide.html', {'sls': sls})

@login_required(login_url='/users/login/')
def save_slide_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            sls = serviceimg.objects.all().order_by('-service_id')
            data['html_site_list'] = render_to_string('sitemanages/slide/partial_slide_list.html', {
                'sls': sls
            })
            return HttpResponseRedirect('/site/slide/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def slide_create(request):
    if request.method == 'POST':
        form = SlideForm(request.POST,request.FILES)
    else:
        form = SlideForm()
    return save_slide_form(request, form, 'sitemanages/slide/partial_slide_create.html')

@login_required(login_url='/users/login/')
def slide_update(request, pk):
    sl = get_object_or_404(serviceimg, pk=pk)
    if request.method == 'POST':
        form = SlideForm(request.POST,request.FILES, instance=sl)
    else:
        form = SlideForm(instance=sl)
    return save_slide_form(request, form, 'sitemanages/slide/partial_slide_update.html')


@login_required(login_url='/users/login/')
def slide_delete(request, pk):
    sl = get_object_or_404(serviceimg, pk=pk)
    data = dict()
    if request.method == 'POST':
        sl.delete()
        data['form_is_valid'] = True
        sls = serviceimg.objects.all().order_by('-service_id')
        data['html_site_list'] = render_to_string('sitemanages/slide/partial_slide_list.html', {
            'sls': sls
        })
        return HttpResponseRedirect('/site/slide/')
    else:
        context = {'sl': sl}
        data['html_form'] = render_to_string('sitemanages/slide/partial_slide_delete.html', context, request=request)
    return JsonResponse(data)


#index > faq
def faq_frontpage(request):
    faqs = faqsite.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})
@login_required(login_url='/users/login/')
def faq_list(request):
    faqs = faqsite.objects.all()
    return render(request, 'sitemanages/manage_faq.html', {'faqs': faqs})

@login_required(login_url='/users/login/')
def save_faq_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            faqs = faqsite.objects.all()
            data['html_faq_list'] = render_to_string('sitemanages/faqs/partial_faq_list.html', {
                'faqs': faqs
            })
            # return HttpResponseRedirect('/site/slide/')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url='/users/login/')
def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
    else:
        form = FAQForm()
    return save_faq_form(request, form, 'sitemanages/faqs/partial_faq_create.html')

@login_required(login_url='/users/login/')
def faq_update(request, pk):
    faq = get_object_or_404(faqsite, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
    else:
        form = FAQForm(instance=faq)
    return save_faq_form(request, form, 'sitemanages/faqs/partial_faq_update.html')


@login_required(login_url='/users/login/')
def faq_delete(request, pk):
    faq = get_object_or_404(faqsite, pk=pk)
    data = dict()
    if request.method == 'POST':
        faq.delete()
        data['form_is_valid'] = True
        faqs = faqsite.objects.all()
        data['html_faq_list'] = render_to_string('sitemanages/faqs/partial_faq_list.html', {
            'faqs': faqs
        })
    else:
        context = {'faq': faq}
        data['html_form'] = render_to_string('sitemanages/faqs/partial_faq_delete.html', context, request=request)
    return JsonResponse(data)
