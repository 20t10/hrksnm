from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import TemplateView,ListView,DetailView

from branches.models import Branch
from sitemanages.models import managesite,serviceimg, faqsite

class IndexView(ListView):
    template_name = 'index.html'
    model = managesite
    def get_context_data(self, **kwargs):
        context = {}
        manage_site = managesite.objects.all()
        context['manage_site'] = manage_site
        branch_list = Branch.objects.all()
        context['branch_list'] = branch_list
        sls = serviceimg.objects.all()
        context['sls'] = sls
        faqs = faqsite.objects.all()
        context['faqs'] = faqs
        return context

class ShowBranch(ListView):
    template_name = 'branches.html'
    model = Branch
    context_object_name = 'branch_list'
    paginate_by = 2

class Errorpage(TemplateView):
    def get_template_names(self):
        template_name = 'error.html'
        return template_name