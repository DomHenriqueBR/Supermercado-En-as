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

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'mercado/categoria_list.html', {'categorias': categorias})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'mercado/cliente_list.html', {'clientes': clientes})

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'mercado/pedido_list.html', {'pedidos': pedidos})