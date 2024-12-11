"""
URL configuration for eneas_sj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mercado import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('categorias/create/', views.categoria_create, name='categoria_create'),
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('pedidos/create/', views.pedido_create, name='pedido_create'),
    path('produtos/create/', views.produto_create, name='produto_create'),
]