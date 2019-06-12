from django.urls import path
from branches import views
app_name ='branches'


urlpatterns = [
#branch
    path('branches/',views.branch_list,name='branches_list'),
    path('<int:pk>/',views.BranchDetail.as_view(),name='branch-detail'),
    path('bo/<int:pk>/',views.detail_owner,name='bo'),
    path('branches/create/',views.branch_create,name='branch_create'),
    path('branches/<int:pk>/update',views.branch_update,name='branch_update'),
    path('branches/<int:pk>/delete',views.branch_delete,name='branch_delete'),
# Monthly
    # path('monthly/',views.monthly_list,name='monthly_list'),
    # path('monthly/create/',views.monthly_create,name='monthly_create'),
    # path('monthly/<int:pk>/update',views.monthly_update,name='monthly_update'),
    # path('monthly/<int:pk>/delete',views.monthly_delete,name='monthly_delete'),

#withdraw CreateWithdraw
    path('withdraw/',views.withdraw_list,name='withdraw_list'),
    path('withdraw/<int:pk>/detail/', views.WithdrawDetail.as_view(), name='withdraw_detail'),
    path('withdraw/create_normal/', views.CreateWithdraw.as_view(), name='wd_normal'),
    path('withdraw/create/',views.withdraw_create,name='withdraw_create'),
    # path('withdraw/create/<int:pk>/',views.withdraw_create,name='withdraw_create'),
    path('withdraw/<int:pk>/update',views.withdraw_update,name='withdraw_update'),
    path('withdraw/<int:pk>/delete',views.withdraw_delete,name='withdraw_delete'),
]
