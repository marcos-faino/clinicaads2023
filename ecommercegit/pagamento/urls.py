from django.urls import path
from . import views

app_name = 'pagamento'

urlpatterns=[
    path('processar/', views.ProcessarPagamentoView.as_view(), name='processar'),
    path('realizado/', views.PagamentoRealizado.as_view(), name='realizado'),
    path('cancelado/', views.PagamentoCancelado.as_view(), name='cancelado'),
]