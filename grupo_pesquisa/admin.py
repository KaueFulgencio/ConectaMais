from django.contrib import admin

# Register your models here.

from .models import Integrante, Publicacao, GrupoPesquisa

admin.site.register(GrupoPesquisa)

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nome', 'tipo')

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'onde_publicado', 'integrante')
    list_filter = ('integrante', 'ano_publicacao')
    search_fields = ('titulo', 'onde_publicado', 'integrante__nome')
