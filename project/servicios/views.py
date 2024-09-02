from django.shortcuts import render
from .models import Cliente, Servicio, Pedido
from .forms import ClienteForm, PedidoForm, ServicioForm

def index(request):
    return render(request, "servicios/index.html")

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/cliente_list.html", context)

def servicio_list(request):
    query = Servicio.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/servicio_list.html", context)

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/pedido_list.html", context)







def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "servicios/cliente_create.html", {"form": form})

def servicio_create(request):
    if request.method == "GET":
        form = ServicioForm()  # Cambiado a ServicioForm
    if request.method == "POST":
        form = ServicioForm(request.POST)  # Cambiado a ServicioForm
        if form.is_valid():
            form.save()
            return redirect("servicio_list")
    return render(request, "servicios/servicio_create.html", {"form": form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()  # Cambiado a ServicioForm
    if request.method == "POST":
        form = PedidoForm(request.POST)  # Cambiado a ServicioForm
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "servicios/pedido_create.html", {"form": form})