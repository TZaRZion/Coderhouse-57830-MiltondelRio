from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Cliente, Servicio, Pedido, Usuario


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
        queryset=Cliente.objects.all(), empty_label="Seleccione un cliente"
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

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto_perfil', 'password1', 'password2']

class PerfilForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto_perfil']