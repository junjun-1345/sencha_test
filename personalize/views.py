from django.shortcuts import render
from django.views import generic

from . forms import DiagnoseForm
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class DiagnoseView(generic.FormView):
    template_name = "diagnose.html"
    form_class = DiagnoseForm