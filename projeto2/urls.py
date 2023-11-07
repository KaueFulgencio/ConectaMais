"""
URL configuration for projeto2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from grupo_pesquisa import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.descricao_grupo, name='descricao_grupo'),
    path('lista_integrantes/', views.lista_integrantes, name='lista_integrantes'),
    path('integrante/<int:integrante_id>/', views.detalhes_integrante, name='detalhes_integrante'),
    path('adicionar_foto_integrante/<int:integrante_id>/', views.adicionar_foto_integrante, name='adicionar_foto_integrante'),
    path('adicionar_integrante/', views.adicionar_integrante, name='adicionar_integrante'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)