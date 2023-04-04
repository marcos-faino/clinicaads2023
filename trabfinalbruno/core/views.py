from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

from core.models import Tecnico, Atendimento

class IndexView(TemplateView):
    template_name = 'index.html'

class ListarTecnicoView(ListView):
    model = Tecnico
    template_name = 'listartecnicos.html'
    queryset = Tecnico.objects.all()
    context_object_name = 'tecnicos'

class CadastraTecnicosView(CreateView):
    model = Tecnico
    template_name = 'formtecnico.html'
    fields = ['nome']
    success_url = reverse_lazy('listartecnico')

class AtualizarTecnicosView(UpdateView):
    model = Tecnico
    template_name = 'formtecnico.html'
    fields = ['nome']
    success_url = reverse_lazy('listaratendimento')


class ExcluirTecnicosView(DeleteView):
    model = Tecnico
    template_name = 'excluirtecnico.html'
    success_url = reverse_lazy('listartecnico')

# Atendimento

class ListarAtendimentosView(ListView):
    model = Atendimento
    template_name = 'listaratendimento.html'
    queryset = Atendimento.objects.all()
    context_object_name = 'atendimentos'

class CadastraAtendimentosView(CreateView):
    model = Atendimento
    template_name = 'formatendimento.html'
    fields = ['descricao', 'preco', 'quantidade', 'tecnico']
    success_url = reverse_lazy('listaratendimento')

class AtualizarAtendimentosView(UpdateView):
    model = Atendimento
    template_name = 'formatendimento.html'
    fields = ['descricao', 'preco', 'quantidade', 'tecnico']
    success_url = reverse_lazy('listaratendimento')


class ExcluirAtendimentosView(DeleteView):
    model = Atendimento
    template_name = 'excluiratendimento.html'
    success_url = reverse_lazy('listartecnico')

