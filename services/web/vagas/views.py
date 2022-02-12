from django.shortcuts import render, get_object_or_404
from .forms import CadastroVagasForm
from .models import Vaga

def detail_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)
    
    return render(request, 'oportunidades_detail.html', {'vaga': vaga})

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
