from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from datetime import datetime as dt
from .forms import CadastroVagasForm
from .models import Vaga
from vagas.templatetags.vagas_template_extras import phone_formatter

def delete_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)

    return render(request, 'oportunidades_delete.html', {'vaga': vaga})

def edit_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)
    form = CadastroVagasForm({
        'empresa_nome': vaga.empresa_nome,
        'empresa_endereco': vaga.empresa_endereco,
        'empresa_email': vaga.empresa_email,
        'empresa_site': vaga.empresa_site,
        'empresa_telefone_celular': phone_formatter(vaga.empresa_telefone_celular),
        'empresa_telefone_comercial': phone_formatter(vaga.empresa_telefone_comercial),
        'cargo_titulo': vaga.cargo_titulo,
        'cargo_descricao': vaga.cargo_descricao,
        'site_referencia': vaga.site_referencia,
        'data_hora_entrevista': dt.strftime(timezone.localtime(vaga.data_hora_entrevista), 
            '%d/%m/%Y %H:%M'),
    })

    return render(request, 'oportunidades_edit.html', {'form': form})

def detail_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)
    
    return render(request, 'oportunidades_detail.html', {'vaga': vaga})

def create_view(request):
    if 'POST' == request.method:
        form = CadastroVagasForm(request.POST)

        if form.is_valid():
            vaga = Vaga.objects.create(
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
            messages.add_message(request, messages.SUCCESS, 'Vaga registrada com sucesso.')
            
            return redirect(reverse('oportunidades_detail', args=[str(vaga.id)]))
    else:
        form = CadastroVagasForm()
    
    return render(request, 'oportunidades_new.html', {'form': form})
