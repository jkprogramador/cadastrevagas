from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from vagas.forms import CadastroVagasForm
from vagas.models import Vaga

def index(request):
    vagas = Vaga.objects.all()

    return render(request, 'homepage.html', {'vagas': vagas})

def delete_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)

    if request.method == 'POST':
        vaga.delete()
        messages.add_message(request, messages.SUCCESS, 'Vaga removida com sucesso.')

        return redirect(reverse('homepage'))

    return render(request, 'oportunidades_delete.html', {'vaga': vaga})

def edit_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)
    form = CadastroVagasForm(initial={
        'empresa_nome': vaga.empresa_nome,
        'empresa_endereco': vaga.empresa_endereco,
        'empresa_email': vaga.empresa_email,
        'empresa_site': vaga.empresa_site,
        'empresa_telefone_celular': vaga.empresa_telefone_celular,
        'empresa_telefone_comercial': vaga.empresa_telefone_comercial,
        'cargo_titulo': vaga.cargo_titulo,
        'cargo_descricao': vaga.cargo_descricao,
        'site_referencia': vaga.site_referencia,
        'data_hora_entrevista': timezone.localtime(vaga.data_hora_entrevista).strftime('%d/%m/%Y %H:%M') if vaga.data_hora_entrevista is not None else '',
        'situacao': vaga.situacao,
    })

    if request.method == 'POST':
        form = CadastroVagasForm(request.POST)

        if form.is_valid():
            vaga.empresa_nome = form.cleaned_data['empresa_nome']
            vaga.empresa_endereco = form.cleaned_data['empresa_endereco']
            vaga.empresa_email = form.cleaned_data['empresa_email']
            vaga.empresa_site = form.cleaned_data['empresa_site']
            vaga.empresa_telefone_celular = form.cleaned_data['empresa_telefone_celular']
            vaga.empresa_telefone_comercial = form.cleaned_data['empresa_telefone_comercial']
            vaga.cargo_titulo = form.cleaned_data['cargo_titulo']
            vaga.cargo_descricao = form.cleaned_data['cargo_descricao']
            vaga.site_referencia = form.cleaned_data['site_referencia']
            vaga.data_hora_entrevista = form.cleaned_data['data_hora_entrevista']
            vaga.situacao = form.cleaned_data['situacao']
            vaga.save()
            messages.add_message(request, messages.SUCCESS, 'Vaga atualizada com sucesso.')

            return redirect(reverse('oportunidades_detail', args=[str(vaga.pk)]))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu um erro ao atualizar o cadastro. Por favor, verifique os dados preenchidos.')

    return render(request, 'oportunidades_edit.html', {'form': form})

def detail_view(request, pk: int):
    vaga = get_object_or_404(Vaga, pk=pk)
    
    return render(request, 'oportunidades_detail.html', {'vaga': vaga})

def create_view(request):
    form = CadastroVagasForm()
    
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
                situacao=form.cleaned_data['situacao'],
            )
            messages.add_message(request, messages.SUCCESS, 'Vaga registrada com sucesso.')
            
            return redirect(reverse('oportunidades_detail', args=[str(vaga.id)]))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu um erro no cadastro. Por favor, verifique os dados preenchidos.')
    
    return render(request, 'oportunidades_new.html', {'form': form})
