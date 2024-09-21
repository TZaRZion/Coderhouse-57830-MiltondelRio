from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Servicio, Pedido
from .forms import ClienteForm, PedidoForm, ServicioForm, BuscarClienteForm, RegistroForm, PerfilForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



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
            return redirect("servicios:cliente_list")
    return render(request, "servicios/cliente_create.html", {"form": form})

def servicio_create(request):
    if request.method == "GET":
        form = ServicioForm()  
    if request.method == "POST":
        form = ServicioForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("servicios:servicio_list")
    return render(request, "servicios/servicio_create.html", {"form": form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()  
    if request.method == "POST":
        form = PedidoForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("servicios:pedido_list")
    return render(request, "servicios/pedido_create.html", {"form": form})




def buscar_cliente(request):
    form = BuscarClienteForm()
    resultados = None

    if request.method == "GET" and "query" in request.GET:
        form = BuscarClienteForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Cliente.objects.filter(nombre__icontains=query)

    return render(request, "servicios/buscar_cliente.html", {"form": form, "resultados": resultados})


    

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'servicios/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('servicios:index')
    else:
        form = AuthenticationForm()
    return render(request, 'servicios/login.html', {'form': form})

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'servicios/profile.html', {'form': form})


def pagina_cierre_sesion(request):
    return render(request, 'servicios/logout.html')

def about_view(request):
    return render(request, 'servicios/about.html')



# Actualizar cliente
def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, id=id)  
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)  
        if form.is_valid():
            form.save()  
            return redirect('servicios:cliente_list')  
    else:
        form = ClienteForm(instance=cliente)  
    return render(request, 'servicios/cliente_update.html', {'form': form})


# Eliminar cliente
def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete() 
        return redirect('servicios:cliente_list') 
    return render(request, 'servicios/cliente_delete.html', {'cliente': cliente})


# Detalle de un cliente
def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, id=id)  
    return render(request, "servicios/cliente_detail.html", {"cliente": cliente})
