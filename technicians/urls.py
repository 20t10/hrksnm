from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from technicians import views
app_name = 'teches'


urlpatterns = [

    path('todo/', views.todo_list, name='todo_list'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/<int:pk>/update/', views.todo_update, name='todo_update'),
    path('todo/<int:pk>/delete', views.todo_delete, name='todo_delete'),

    path('tech/', views.tech_todo, name='tech_todo'),
    path('log_todo/', views.log_todo, name='log_todo'),
    path('alllog_todo/', views.alllog_todo, name='alllog_todo'),
    path('work/create/', views.work_create, name='work_create'),
    path('work/<int:pk>/update', views.work_update, name='work_update'),
    path('work/<int:pk>/delete', views.work_delete, name='work_delete'),
    
    #chart
    path('show-noti/', views.ChartView.as_view(), name='show-noti'),
    path('show-chart-money/', views.ChartMoneyView.as_view(), name='show_chart_money'),
    path('fixed-branch/', views.ChartFixedBranchData.as_view(), name='fixed_branch'),
    path('show-fixed-money/', views.ChartFixedView.as_view(), name='show_fixed_money'),
    path('money-branch/', views.ChartMoneyBranchData.as_view(), name='money_branch'),
    path('stat-noti/', views.ChartNotiData.as_view(), name='stat-noti'),
    path('broke_list/', views.ShowBroken, name='broke_list'),

    path('fix_send_form/', views.SendNotification.as_view(), name='fix_send_form'),
    # path('notification/', views.send_notification, name='notification'),
    path('ajax/load-machines/', views.load_machines, name='ajax_load_machines'),  # <-- this one here


    path('noti_list/', views.noti_list, name='noti_list'),
    path('noti/create/', views.noti_create, name='noti_create'),
    path('noti_repair/<int:pk>/', views.noti_update, name='noti_repair'),
    path('noti/<int:pk>/delete', views.noti_delete, name='noti_delete'),

    path('maintaine/', views.maintaine_list, name='maintaine_list'),
    path('maintaine_log/', views.maintaine_log, name='maintaine_log'),
    path('tech-maintaine-log/', views.tech_maintaine_log, name='tech-maintaine-log'),
    path('maintaine/create/', views.maintaine_create, name='maintaine_create'),
    path('maintaine/<int:pk>/update/', views.maintaine_update, name='maintaine_update'),
    path('tech_list/', views.tech_maintaine_list, name='maintaine_tech_list'),
    path('tech/<int:pk>/update/', views.maintaine_tech, name='maintaine_tech'),
    path('maintaine/<int:pk>/delete', views.maintaine_delete, name='maintaine_delete'),
    ]
if settings.DEBUG:
    urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)