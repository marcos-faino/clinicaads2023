from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from carrinho.carrinho import Carrinho
from pedidos.forms import PedidoModelForm
from .models import ItemPedido, Pedido


class PedidoCreateView(CreateView):
    form_class = PedidoModelForm
    success_url = reverse_lazy('resumopedido')
    template_name = 'formpedido.html'

    def form_valid(self, form):
        car = Carrinho(request=self.request)
        pedido = form.save()
        for item in car:
            ItemPedido.objects.create(pedido=pedido,
                                      produto=item['produto'],
                                      preco=item['preco'],
                                      quantidade=item['quantidade'])
        car.limpar()
        pedido = form.save()
        # enviando email de confirmação
        self._emailconfirmacao(pedido)
        self.request.session['idpedido'] = pedido.id
        return redirect('resumopedido', idpedido=pedido.id)

    def _emailconfirmacao(self, pedido):
        conteudo = (f'Obrigado por comprar conosco!!!\n '
                     f'Seu Pedido:\n')

        for item in pedido.itens_pedido.all():
            conteudo += (f'{item.produto.nome}\t\t{item.quantidade}\t{item.preco}\t'
                         f'R${item.get_custo()}\n')
        conteudo += f'Total\t\t\t\tR${pedido.get_total()}\n'
        mail = EmailMessage(
            subject=f'Contato de {pedido.nome}',
            body=conteudo,
            from_email='marcosfaino@gmail.com',
            to=[f'{ pedido.email }', ],
        )
        mail.send()


class ResumoPedidoTemplateView(TemplateView):
    template_name = 'resumopedido.html'

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['pedido'] = Pedido.objects.get(id=self.kwargs['idpedido'])
        return contexto
