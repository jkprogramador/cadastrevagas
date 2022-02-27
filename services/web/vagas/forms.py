from django import forms
from django.core.validators import RegexValidator

class CadastroVagasForm(forms.Form):
    """Form for submitting job opportunities."""
    template_name = 'cadastro_vagas_form.html'

    empresa_nome = forms.CharField(
        label='Nome da empresa',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
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
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        max_length=200,
        error_messages={
            'max_length': 'O campo Endereço da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_email = forms.EmailField(
        label='Email da empresa',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: empresa@email.com.br'
        }),
        required=False,
        error_messages={
            'invalid': 'O campo Email da empresa deve conter um email válido.'
        }
    )

    empresa_site = forms.URLField(
        label='Site da empresa',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
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
            'class': 'form-control',
            'placeholder': '(DDD) 99999-9999'
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
            'class': 'form-control',
            'placeholder': '(DDD) 9999-9999',
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
            'class': 'form-control',
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
            'class': 'form-control'
        }),
        label='Descrição do cargo',
        required=False
    )

    site_referencia = forms.URLField(
        label='Site de referência',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
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
            'type': 'datetime',
            'class': 'form-control',
            'aria-describedby': 'data_hora_entrevista_help'
        }, format='%d/%m/%Y %H:%M'),
        label='Data e horário da entrevista',
        help_text='Ex.: dia/mês/ano horas:minutos',
        required=False,
        error_messages={
            'invalid': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos'
        }
    )