from django.shortcuts import render
from django.views import generic
from . forms import DiagnoseForm
from .models import Tea

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class DiagnoseView(generic.FormView):
    template_name = "diagnose.html"
    form_class = DiagnoseForm


class DiagnoseListView(generic.ListView):
    model = Tea
    template_name = 'diagnose_list.html'

