from django.urls import path

from owners import views

app_name = 'owner'

urlpatterns = [
    path('',views.owner_list,name='owner_list'),
    path('manage/<int:pk>/',views.OwnerManage.as_view(),name='manage'),
    path('manage_branch/',views.OwnerShowList.as_view(),name='manage_branch'),
    path('machine-list/<int:pk>/',views.OwnerBranchList.as_view(),name='owner_machine_list'),
    path('benefit_branch/',views.OwnerBenefitbranch.as_view(),name='benefit_branch'),
    path('benefit/<int:pk>/',views.OwnerBenefit.as_view(),name='benefit'),
    path('noti/<int:pk>/',views.OwnerNoti.as_view(),name='noti'),
    path('detail/<int:pk>/',views.OwnerBranchDetail.as_view(),name='detail'),
    path('module/',views.OwnerBranchDetail.as_view(),name='module'),
    path('owner/create/',views.owner_create,name='owner_create'),
    path('owner/<int:pk>/update',views.owner_update,name='owner_update'),
    path('owner/<int:pk>/delete',views.owner_delete,name='owner_delete'),
]
