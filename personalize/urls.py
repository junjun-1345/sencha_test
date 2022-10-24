from django.urls import path

from . import views


app_name = 'personalize'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('diagnose/', views.diagnose, name="diagnose"),
    path('diagnose_list/', views.DiagnoseListView.as_view(), name="diagnose_list"),
    path('result/', views.ResultView.as_view(), name="result"),
]