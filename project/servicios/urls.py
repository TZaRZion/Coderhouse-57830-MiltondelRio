# servicios/urls.py
from django.urls import path
from . import views

app_name = 'servicios' 

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/list/', views.cliente_list, name='cliente_list'),
    path('servicio/list/', views.servicio_list, name='servicio_list'),
    path('pedido/list/', views.pedido_list, name='pedido_list'),
    path('cliente/create/', views.cliente_create, name='cliente_create'),
    path('servicio/create/', views.servicio_create, name='servicio_create'),
    path('pedido/create/', views.pedido_create, name='pedido_create'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
    path('registro/', views.registro_view, name='register'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('login/', views.login_view, name='login'),
    path('pagina-cierre-sesion/', views.pagina_cierre_sesion, name='pagina_cierre_sesion'),
    path('about/', views.about_view, name='about'),
    
    # Nuevas rutas para el CRUD de clientes
    path('cliente/<int:id>/', views.cliente_detail, name='cliente_detail'),  # Ver detalles
    path('cliente/<int:id>/editar/', views.cliente_update, name='cliente_update'),  # Editar
    path('cliente/<int:id>/eliminar/', views.cliente_delete, name='cliente_delete'),  # Eliminar


]
