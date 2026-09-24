from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteDeleteView,
    TransaccionCreateView,
)

urlpatterns = [
    path("", ClienteListView.as_view(), name="lista_clientes"),
    path("clientes/crear/", ClienteCreateView.as_view(), name="crear_cliente"),
    path("clientes/<int:pk>/", ClienteDetailView.as_view(), name="detalle_cliente"),
    path("clientes/<int:pk>/editar/", ClienteUpdateView.as_view(), name="editar_cliente"),
    path("clientes/<int:pk>/eliminar/", ClienteDeleteView.as_view(), name="eliminar_cliente"),
    path("cuentas/<int:cuenta_id>/transaccion/crear/", TransaccionCreateView.as_view(), name="crear_transaccion"),
]