from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('consconv/', views.GraficosConsultasView.as_view(), name='consconv'),
    path('consmed/', views.MedicosAtendView.as_view(), name='consmed'),
]