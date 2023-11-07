from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404

#modelos
from .models import Integrante, Publicacao, GrupoPesquisa
from .forms import IntegranteForm, PublicacaoForm

def descricao_grupo(request):
    return render(request, 'descricao_grupo.html')

def lista_integrantes(request):
    integrantes = Integrante.objects.all()
    return render(request, 'lista_integrantes.html', {'integrantes': integrantes})

def detalhes_integrante(request, integrante_id):
    integrante = get_object_or_404(Integrante, pk=integrante_id)
    publicacoes = integrante.publicacoes.all()
    publicacoes_disponiveis = Publicacao.objects.all()
    
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            if 'publicacao_id' in request.POST:
                # Se um ID de publicação foi fornecido, use a publicação existente
                publicacao = get_object_or_404(Publicacao, pk=request.POST['publicacao_id'])
            else:
                # Se não for fornecido um ID de publicação, crie uma nova publicação
                publicacao = form.save()
            integrante.publicacoes.add(publicacao)

    form = PublicacaoForm()
    
    return render(request, 'detalhes_integrante.html', {
        'integrante': integrante,
        'publicacoes': publicacoes,
        'publicacoes_disponiveis': publicacoes_disponiveis,
        'form': form,
    })

def adicionar_foto_integrante(request, integrante_id):
    integrante = Integrante.objects.get(pk=integrante_id)

    if request.method == 'POST':
        integrante.foto = request.FILES['foto']
        integrante.save()

        return redirect('detalhes_integrante', integrante_id=integrante.id)

    return render(request, 'adicionar_foto_integrante.html', {'integrante': integrante})

def descricao_grupo(request):
    grupos_pesquisa = GrupoPesquisa.objects.all()  
    return render(request, 'descricao_grupo.html', {'grupos_pesquisa': grupos_pesquisa})

def adicionar_integrante(request):
    if request.method == 'POST':
        form = IntegranteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_integrantes')
    else:
        form = IntegranteForm()
    
    return render(request, 'adicionar_integrante.html', {'form': form})

from grupo_pesquisa.models import GrupoPesquisa 

grupo_pesquisa = GrupoPesquisa(nome='GRUPO DE PESQUISA 1', descricao='Processo de criação em andamento...')

grupo_pesquisa.save()
