"""sainammint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from .views import IndexView,ShowBranch, Errorpage
from sitemanages.views import faq_frontpage
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('faqs/',faq_frontpage,name='faqs'),
    path('branch',ShowBranch.as_view(),name='branch'),
    path('users/',include('users.urls',namespace="users")),
    path('branches/',include('branches.urls',namespace="branches")),
    path('owners/',include('owners.urls',namespace="owners")),
    path('teches/',include('technicians.urls',namespace="teches")),
    path('machines/',include('machines.urls',namespace="machines")),
    path('profits/', include('profits.urls')),
    path('site/',include('sitemanages.urls',namespace="site")),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),

    # re_path(r"^.*", Errorpage.as_view(),name='error-page' ),
]
if settings.DEBUG:
    urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
