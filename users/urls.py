from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
app_name ='users'
urlpatterns = [
    # authenticate
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('change_password/',views.change_password,name='change_password'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    # user manage
    path('dashboard/',views.user_list_manage,name='dashboard'),
    path('users/',views.user_list,name='user_list'),
    # path('users/',views.user_list_manage,name='user_list'),
    path('users/create/',views.user_create,name='user_create'),
    path('users/<int:pk>/update',views.user_update,name='user_update'),
    path('users/<int:pk>/delete',views.user_delete,name='user_delete'),
]
