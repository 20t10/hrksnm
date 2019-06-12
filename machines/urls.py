from django.urls import path

from machines import views
app_name ='machines'
urlpatterns = [
    path('machines/',views.machine_list,name='machine_list'),# main crud
    path('income/',views.machine_income,name='machine_income'),#รายได้
    path('machines/create/',views.machine_create,name='machine_create'),
    path('machines/<int:pk>/update',views.machine_update,name='machine_update'),
    path('machines/<int:pk>/delete',views.machine_delete,name='machine_delete'),
    #module
    path('list/', views.machine_list_module, name='list'),
    path('detail/<int:pk>/', views.machine_detail_module, name='detail'),
    #api
    path('details/', views.MachineListAPIView.as_view(),name='details'),

    path('log/<int:pk>/',views.MachineLogAPIView.as_view(),name='log'),
    path('real/<int:pk>/',views.MachineRealAPIView.as_view(),name='real'),

    path('machine_detail_coin/',views.machine_detail_coin,name='machine_detail_coin'),
    path('machine_coin/<int:pk>/',views.MachineListBranchAPIView.as_view(),name='machine_coin'),


    #real
    path('realtime/', views.real_list, name='realtime_list'),
    path('realtime/create/', views.real_create, name='realtime_create'),
    path('realtime/<int:pk>/update', views.real_update, name='realtime_update'),
    path('realtime/<int:pk>/delete', views.real_delete, name='realtime_delete'),
    # log
    path('log/', views.log_list, name='log_list'),
    path('log/create/', views.log_create, name='log_create'),
    path('log/<int:pk>/update', views.log_update, name='log_update'),
    path('log/<int:pk>/delete', views.log_delete, name='log_delete'),
]
