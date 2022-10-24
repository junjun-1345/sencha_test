from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import DiagnoseForm
from .models import Tea
from django.shortcuts import redirect


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


def diagnose(request):
    params = {
        'num': 0,
        'form': DiagnoseForm(),
    }

    if request.method == 'POST':
        if 'check' in request.POST:
            request.session['form_data'] = request.POST
            params['form'] = DiagnoseForm(request.POST)
            return render(request, 'result.html', params)

        while True:
            if 'next' in request.POST:
                params['num'] = params['num'] + int(1)
                return render(request, 'diagnose.html', params)

            if 'back' in request.POST:
                params['num'] = params['num'] - int(1)
            return render(request, 'diagnose.html', params)

    return render(request, 'diagnose.html', params)

# class DiagnoseView(generic.FormView):
#     template_name = "diagnose.html"
#     form_class = DiagnoseForm
#     success_url = reverse_lazy('personalize:result')
#
#     def form_valid(self, form):
#         self.request.session['form_data'] = self.request.POST
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['message'] = 'Get処理'
#
#         return context
#
#         # get処理
#
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class DiagnoseListView(generic.ListView):
    model = Tea
    template_name = 'diagnose_list.html'


class ResultView(generic.TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_data = self.request.session.get('form_data', None)
        context['form'] = DiagnoseForm(form_data)
        return context
