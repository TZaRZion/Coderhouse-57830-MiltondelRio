from django.contrib import admin
from .models import Cliente, Servicio, Pedido


# admin.site.register(Cliente)
# admin.site.register(Servicio)
# admin.site.register(Pedido)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "celular")
    search_fields = ("nombre", "apellido", "celular")
    ordering = ("apellido", "nombre")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponible")
    list_filter = ("disponible",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "servicio", "estado", "fecha_solicitud", "fecha_entrega")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "servicio__nombre")
    ordering = ("-fecha_entrega",)
    date_hierarchy = "fecha_solicitud"