
from django.shortcuts import render, get_object_or_404, redirect, reverse

from ecommerce import settings
from pedidos.models import Pedido
from django.views.generic import FormView, TemplateView

import braintree

from . import forms


class ProcessarPagamentoView(FormView):
    """This view lets the user initiate a payment."""
    form_class = forms.CheckoutForm
    template_name = 'pagamento/processar.html'

    def dispatch(self, request, *args, **kwargs):

        # Ha! There it is. This allows you to switch the
        # Braintree environments by changing one setting

        braintree_env = braintree.Environment.Sandbox
        # Configure Braintree
        braintree.Configuration.configure(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )

        # Generate a client token. We'll send this to the form to
        # finally generate the payment nonce
        # You're able to add something like ``{"customer_id": 'foo'}``,
        # if you've already saved the ID
        self.braintree_client_token = braintree.ClientToken.generate({})
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'braintree_client_token': self.braintree_client_token,
        })
        return ctx

    def form_valid(self, form):
        idpedido = self.request.session.get('idpedido')
        pedido = get_object_or_404(Pedido, id=idpedido)
        custo_total = pedido.get_total()
        result = braintree.Transaction.sale({
            "amount": custo_total,
            "payment_method_nonce": form.cleaned_data['payment_method_nonce'],
            "options": {
                'submit_for_settlement': True,
            },
        })
        if not result.is_success:
            # Card could've been declined or whatever
            # I recommend to send an error report to all admins
            # , including ``result.message`` and ``self.user.email``
            context = self.get_context_data()
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error':
                    'Pagamento não processado. Por favor verifique'
                    ' os dados e tente novamente.'
            })
            return self.render_to_response(context)

        # Finally there's the transaction ID
        # You definitely want to send it to your database
        transaction_id = result.transaction.id
        # Now you can send out confirmation emails or update your metrics
        # or do whatever makes you and your customers happy :)
        return super().form_valid(form)

    def get_success_url(self):
        # Add your preferred success url
        return reverse('pagamento:realizado')


class PagamentoRealizado(TemplateView):
    template_name = 'pagamento/realizado.html'


class PagamentoCancelado(TemplateView):
    template_name = 'pagamento/cancelado.html'
