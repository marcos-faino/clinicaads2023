from django.urls import path
from .views import IndexView, ListarTecnicoView, CadastraTecnicosView, AtualizarTecnicosView, ExcluirTecnicosView, ListarAtendimentosView, CadastraAtendimentosView, AtualizarAtendimentosView, ExcluirAtendimentosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_tecnico/', ListarTecnicoView.as_view(), name='listartecnico'),
    path('cadastrar_tecnico/', CadastraTecnicosView.as_view(), name='cadastrartecnico'),
    path('atualizar_tecnico/<int:pk>', AtualizarTecnicosView.as_view(), name='atualizartecnico'),
    path('excluir_tecnico/<int:pk>', ExcluirTecnicosView.as_view(), name='excluirtecnico'),

    path('listar_atendimento/', ListarAtendimentosView.as_view(), name='listaratendimento'),
    path('cadastrar_atendimento/', CadastraAtendimentosView.as_view(), name='castraratendimento'),
    path('atualizar_atendimento/<int:pk>', AtualizarAtendimentosView.as_view(), name='atualizaratendimento'),
    path('excluir_atendimento/<int:pk>', ExcluirAtendimentosView.as_view(), name='excluiratendimento'),
]
