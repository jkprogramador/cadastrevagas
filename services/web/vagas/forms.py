from django import forms
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from vagas.models import Vaga
from vagas.validators import is_equal_to_or_later_than_current_datetime

class CadastroVagasForm(forms.Form):
    """Form for submitting job opportunities."""
    template_name = 'cadastro_vagas_form.html'

    empresa_nome = forms.CharField(
        label='Nome da empresa',
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm',
            'aria-describedby': 'empresa_nome_required'
        }),
        required=True,
        max_length=100,
        error_messages={
            'required': 'O campo Nome da empresa é obrigatório.',
            'max_length': 'O campo Nome da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_endereco = forms.CharField(
        label='Endereço da empresa',
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm',
            'aria-describedby': ''
        }),
        required=False,
        max_length=200,
        error_messages={
            'max_length': 'O campo Endereço da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_email = forms.EmailField(
        label='Email da empresa',
        widget=forms.EmailInput(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': 'Ex.: empresa@email.com.br',
            'aria-describedby': ''
        }),
        required=False,
        error_messages={
            'invalid': 'O campo Email da empresa deve conter um email válido.'
        }
    )

    empresa_site = forms.URLField(
        label='Site da empresa',
        widget=forms.URLInput(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': 'Ex.: https://empresa.com.br',
            'aria-describedby': 'empresa_site_required'
        }),
        required=True,
        error_messages={
            'required': 'O campo Site da empresa é obrigatório.',
            'invalid': 'O campo Site da empresa deve conter um endereço web válido.'
        }
    )

    empresa_telefone_celular = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': '(DDD) 99999-9999',
            'aria-describedby': ''
        }),
        label='Telefone celular da empresa',
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) 9\d{4}-\d{4}$',
                message='O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999',
                code='invalid'
            )
        ]
    )

    empresa_telefone_comercial = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': '(DDD) 9999-9999',
            'aria-describedby': ''
        }),
        label='Telefone comercial da empresa',
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) \d{4}-\d{4}$',
                message='O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999',
                code='invalid'
            )
        ]
    )

    cargo_titulo = forms.CharField(
        label='Título do cargo',
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm',
            'aria-describedby': 'cargo_titulo_required'
        }),
        required=True,
        max_length=50,
        error_messages={
            'required': 'O campo Título do cargo é obrigatório.',
            'max_length': 'O campo Título do cargo pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    cargo_descricao = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control shadow-sm',
            'aria-describedby': ''
        }),
        label='Descrição do cargo',
        required=False
    )

    site_referencia = forms.URLField(
        label='Site de referência',
        widget=forms.URLInput(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': 'https://sitedereferencia.com.br',
            'aria-describedby': 'site_referencia_help site_referencia_required'
        }),
        help_text='O website onde a vaga foi encontrada',
        required=True,
        error_messages={
            'required': 'O campo Site de referência é obrigatório.',
            'invalid': 'O campo Site de referência deve conter um endereço web válido.'
        }
    )
    data_hora_entrevista = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control shadow-sm',
            'aria-describedby': 'data_hora_entrevista_help'
        }, format='%d/%m/%Y %H:%M'),
        label='Data e horário da entrevista',
        help_text='Ex.: dia/mês/ano horas:minutos',
        required=False,
        error_messages={
            'invalid': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos'
        }
    )

    situacao = forms.ChoiceField(
        label='Situação',
        required=True,
        choices=Vaga.Status.choices,
        initial=Vaga.Status.WAITING,
        widget=forms.Select(attrs={
            'class': 'form-select shadow-sm',
            'aria-describedby': 'situacao_required',
            'aria-label': 'Situação do cadastro'
        }),
        error_messages={
            'required': 'O campo Situação é obrigatório.',
            'invalid_choice': 'O campo Situação contém um valor inválido.',
        },
    )

    def clean(self):
        super().clean()
        situacao = self.cleaned_data.get('situacao')
        data_hora_entrevista = self.cleaned_data.get('data_hora_entrevista')

        if situacao == Vaga.Status.WAITING and data_hora_entrevista is not None:
            self.add_error('data_hora_entrevista',
                ValidationError("O campo Data e horário da entrevista deve estar vazio caso a situação do cadastro seja 'Aguardando retorno'.", code='invalid')
            )
        
        if (situacao == Vaga.Status.INTERVIEW_SCHEDULED and data_hora_entrevista is None):
            self.add_error('data_hora_entrevista',
                ValidationError("O campo Data e o horário da entrevista deve ser preenchido caso a situação do cadastro seja 'Entrevista agendada'.", code='required')
            )

        if (situacao == Vaga.Status.INTERVIEW_SCHEDULED
            and
            data_hora_entrevista is not None
            and
            not is_equal_to_or_later_than_current_datetime(data_hora_entrevista)
        ):
            self.add_error('data_hora_entrevista',
                ValidationError("O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.", code='invalid_datetime')
            )

        for bound_field in self:
            if bound_field.errors:
                bound_field.field.widget.attrs.update({
                    'class': bound_field.field.widget.attrs['class'] + ' is-invalid',
                    'aria-describedby': ' '.join([bound_field.field.widget.attrs['aria-describedby'], bound_field.html_name + '_error'])
                })


class OportunidadesFilterForm(forms.Form):
    """Form for filtering job opportunities."""

    class DataHoraCadastroOrder(models.TextChoices):
        OLDEST = 'A', 'Mais antigas'
        NEWEST = 'D', 'Mais recentes'

    template_name = 'oportunidades_filter_form.html'
    situacao = forms.ChoiceField(
        label='Situação',
        required=False,
        choices=Vaga.Status.choices + [(None, 'Todas'),],
        initial=(None, 'Todas',),
        widget=forms.Select(attrs={
            'class': 'form-select form-select-sm shadow-sm',
            'aria-label': 'Filtro de situação da oportunidade de vaga',
        }),
    )

    data_hora_cadastro_order = forms.ChoiceField(
        label='Ordernar por data e hora do cadastro',
        required=False,
        choices=DataHoraCadastroOrder.choices,
        initial=DataHoraCadastroOrder.NEWEST,
        widget=forms.Select(attrs={
            'class': 'form-select form-select-sm shadow-sm',
            'aria-label': 'Filtro para ordenar oportunidades por data e hora do cadastro',
        })
    )