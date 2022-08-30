from django.urls import path

from . import views


app_name = 'personalize'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('diagnose/', views.DiagnoseView.as_view(), name="diagnose"),
    path('diagnose_list/', views.DiagnoseListView.as_view(), name="diagnose_list"),
]