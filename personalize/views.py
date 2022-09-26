from django.shortcuts import render
from django.views import generic
from .models import Tea
from django.db.models import Q


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class DiagnoseView(generic.ListView):
    model = Tea
    template_name = "diagnose.html"
    params = {'msg': 'value'}

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        symptom = Tea.objects.order_by('-id')

        if keyword:
            symptom = symptom.filter(
                Q(symptoms1__icontains=keyword) | Q(symptoms2__icontains=keyword) | Q(symptoms3__icontains=keyword) | Q(symptoms4__icontains=keyword) | Q(symptoms5__icontains=keyword) | Q(symptoms6__icontains=keyword) | Q(symptoms7__icontains=keyword) | Q(symptoms8__icontains=keyword) | Q(symptoms9__icontains=keyword) | Q(symptoms10__icontains=keyword) | Q(symptoms11__icontains=keyword) | Q(symptoms12__icontains=keyword) | Q(symptoms13__icontains=keyword) | Q(symptoms14__icontains=keyword) | Q(
                    symptoms15__contains=keyword))
            return symptom
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "チェックボックス"
        return context


class DiagnoseListView(generic.ListView):
    model = Tea
    template_name = 'diagnose_list.html'
