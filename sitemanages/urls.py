from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name ='site'
urlpatterns = [
    path('site/',views.site_list,name='site_list'),
    path('update/<int:pk>/', views.SiteUpdateView.as_view(), name='update'),
    path('update-site/<int:pk>/', views.index_update, name='update-site'),
    path('site/create/',views.site_create,name='site_create'),
    path('site/<int:pk>/update',views.site_update,name='site_update'),
    path('site/<int:pk>/delete',views.site_delete,name='site_delete'),  
    path('slide/', views.slide_list, name='slide_list'),       
    path('slide/create/', views.slide_create, name='slide_create'),
    path('slide/<int:pk>/update', views.slide_update, name='slide_update'),
    path('slide/<int:pk>/delete', views.slide_delete, name='slide_delete'),      
    path('faq/', views.faq_list, name='faq_list'),    
    path('faq/create/', views.faq_create, name='faq_create'),
    path('faq/<int:pk>/update', views.faq_update, name='faq_update'),
    path('faq/<int:pk>/delete', views.faq_delete, name='faq_delete'),
]
if settings.DEBUG:
    urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

