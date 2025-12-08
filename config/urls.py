"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from loja.views import home
from loja.views import produto_detail
from loja.views import sobre
from loja.views import dashboard
from loja.views import produto_remover
from loja.views import produto_editar
from loja.views import produto_criar
from loja.views import lista_produtos 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produto/<int:id>/', produto_detail, name='produto_detail'),
    path('sobre/', sobre, name='sobre'),
    path('dashboard/', dashboard, name='dashboard'),   
    path('produto/novo/', produto_criar, name='produto_criar'),
    path('produto/editar/<int:id>/', produto_editar, name='produto_editar'),
    path('produto/remover/<int:id>/', produto_remover, name='produto_remover'), 
    path('produtos/', lista_produtos, name='lista_produtos'),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
