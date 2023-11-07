import base64
from io import BytesIO

from django.db.models import Count
from django.http import JsonResponse
from django.views import View

from django.views.generic import TemplateView
from core.models import Consulta, Convenio, Medico
from matplotlib import pyplot as plt



class HomeView(TemplateView):
    template_name = 'home.html'

class GraficosConsultasView(TemplateView):
    template_name = 'dashboard.html'
    model = Consulta

    def _criar_grafico(self):
        # plt.switch_backend('agg')
        convenios = Convenio.objects.all()
        labels = []
        data = []
        for c in convenios:
            quant = Consulta.objects.filter(convenio=c).count()
            if quant > 0:
                labels.append(c.nome)
                data.append(quant)
        plt.pie(data, labels=labels)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        grafico = base64.b64encode(image_png)
        grafico = grafico.decode('utf-8')
        buffer.close()
        return grafico

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        graph = self._criar_grafico()
        qtdconsultas = Consulta.objects.all().count()
        ctx['grafico'] = graph
        ctx['qconsultas'] = qtdconsultas
        return ctx


class MedicosAtendView(TemplateView):
    template_name = 'dashboard2.html'
    model = Consulta

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        medicos = Medico.objects.all()
        data = []
        for m in medicos:
            q = Consulta.objects.filter(medico=m).count()
            data.append(
                {
                    'nome': m.nome,
                    'quant': q
                }
            )
        ctx['dados'] = data
        return ctx


class RelatorioConsultasAno(View):

    def get(self, request, ano):
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        data = []
        labels = []
        # consultas = Consulta.objects.all().values('data__year').annotate(total=Count(id))
        consultasano = Consulta.objects.all().filter(data__year=ano)
        consultas = consultasano.values('data__month').annotate(total=Count(id))
        for i in range(1, 12):
            labels.append(meses[i-1])
            for c in consultas:
                if i == c['data__month']:
                    data.append(c['total'])
            data.append(0)

        return JsonResponse({'labels':labels, 'data': data})


class EscolhaMesView(TemplateView):
    template_name = "dashboardchartjs.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        anos = Consulta.objects.all().values('data__year').distinct()
        ctx['anos'] = anos
        return ctx
