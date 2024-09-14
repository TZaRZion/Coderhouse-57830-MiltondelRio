from django import forms

from .models import Cliente, Servicio, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class BuscarClienteForm(forms.Form):
    query = forms.CharField(label="Buscar Cliente", max_length=100)


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Servicio.objects.all(), empty_label="Seleccione un cliente"
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(disponible=True),
        empty_label="Seleccione un servicio",
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {
            "fecha_entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }
