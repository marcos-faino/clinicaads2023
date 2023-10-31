from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from core.models import Consulta


class RelatorioConsultasAno(View):

    def get(self, request, ano):
        data = []
        labels = []
        consultas = Consulta.objects.all().values('data__year').annotate(total = Count(id))
        for c in consultas:
            labels.append(c['data__year'])
            data.append(c['total'])

        return JsonResponse({'labels':labels, 'data': data})



