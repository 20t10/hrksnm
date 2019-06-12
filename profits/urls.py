from django.urls import path
from profits import views

app_name ="profits"
urlpatterns = [
    path('',views.ProfitsListView.as_view(), name="profit-list")
]
