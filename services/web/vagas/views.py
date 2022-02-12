from django.shortcuts import render
from .forms import CadastroVagasForm
from .models import Vaga

def index(request):
    vaga = Vaga.objects.create(
        empresa_nome='Minha empresa',
        empresa_endereco='Meu endereço',
        empresa_email='meuemail@email.com',
        empresa_site='https://meusite.com.br',
        empresa_telefone_celular='(11) 98765-3201',
        empresa_telefone_comercial='(11) 8765-3201',
        cargo_titulo='Título do cargo',
        cargo_descricao='Descrição do cargo',
        site_referencia='https://sitereferencia.com.br',
        data_hora_entrevista='20/01/2022 15:30',
    )

    return render(request, 'index.html', {'vaga': vaga})

def create_view(request):
    if 'POST' == request.method:
        form = CadastroVagasForm(request.POST)

        if form.is_valid():
            Vaga.objects.create(
                empresa_nome=form.cleaned_data['empresa_nome'],
                empresa_endereco=form.cleaned_data['empresa_endereco'],
                empresa_email=form.cleaned_data['empresa_email'],
                empresa_site=form.cleaned_data['empresa_site'],
                empresa_telefone_celular=form.cleaned_data['empresa_telefone_celular'],
                empresa_telefone_comercial=form.cleaned_data['empresa_telefone_comercial'],
                cargo_titulo=form.cleaned_data['cargo_titulo'],
                cargo_descricao=form.cleaned_data['cargo_descricao'],
                site_referencia=form.cleaned_data['site_referencia'],
                data_hora_entrevista=form.cleaned_data['data_hora_entrevista'],
            )
    else:
        form = CadastroVagasForm()
    
    return render(request, 'oportunidades_new.html', {'form': form})
