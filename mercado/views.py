from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'mercado/index.html')

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'mercado/produto_list.html', {'produtos': produtos})

def produto_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        Produto.objects.create(nome=nome, preco=preco, estoque=estoque)
        return redirect('produto_list')
    return render(request, 'mercado/produto_form.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'mercado/login.html')

# Views dos arquivos de listagem
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'mercado/categoria_list.html', {'categorias': categorias})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'mercado/cliente_list.html', {'clientes': clientes})

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'mercado/pedido_list.html', {'pedidos': pedidos})

# Views dos arquivos de criação de algum novo item
def categoria_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        return redirect('categoria_list')
    return render(request, 'mercado/categoria_create.html')

def cliente_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        telefone = request.POST.get('telefone')

        if User.objects.filter(username=username).exists():
            return render(request, 'mercado/cliente_create.html', {
                'error': 'Nome de usuário já existe.'
            })
        usuario = User.objects.create_user(username=username, password=password)
        Cliente.objects.create(usuario=usuario, telefone=telefone)
        return redirect('cliente_list')
    return render(request, 'mercado/cliente_create.html')


from django.shortcuts import render, redirect
from .models import Produto, Categoria

def produto_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        categorias_ids = request.POST.getlist('categorias')
        produto = Produto.objects.create(nome=nome, preco=preco, estoque=estoque)
        if categorias_ids:
            categorias = Categoria.objects.filter(id__in=categorias_ids)
            produto.categorias.set(categorias) 
        return redirect('produto_list') 
    categorias = Categoria.objects.all()
    return render(request, 'mercado/produto_create.html', {'categorias': categorias})



def pedido_create(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produtos_ids = request.POST.getlist('produtos')
        cliente = Cliente.objects.get(id=cliente_id)
        pedido = Pedido.objects.create(cliente=cliente)
        pedido.produtos.set(produtos_ids) 
        return redirect('pedido_list') 
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'mercado/pedido_create.html', {'clientes': clientes, 'produtos': produtos})