from django import forms
from .models import Integrante, Publicacao, GrupoPesquisa

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'ano_publicacao', 'onde_publicado', 'autores']

    def clean_ano_publicacao(self):
        ano_publicacao = self.cleaned_data.get('ano_publicacao')
        if ano_publicacao is None:
            raise forms.ValidationError("Ano de publicação é obrigatório.")
        return ano_publicacao

        
class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['nome', 'tipo', 'foto']

class GrupoPesquisaForm(forms.ModelForm):
    class Meta:
        model = GrupoPesquisa
        fields = ['nome', 'descricao']
        
        