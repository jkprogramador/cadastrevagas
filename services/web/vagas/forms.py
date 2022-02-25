from django import forms
from django.core.validators import RegexValidator

class CadastroVagasForm(forms.Form):
    """Form for submitting job opportunities."""
    empresa_nome = forms.CharField(
        label='Nome da empresa',
        required=True,
        max_length=100,
        error_messages={
            'required': 'O campo Nome da empresa é obrigatório.',
            'max_length': 'O campo Nome da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_endereco = forms.CharField(
        label='Endereço da empresa',
        required=False,
        max_length=200,
        error_messages={
            'max_length': 'O campo Endereço da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_email = forms.EmailField(
        label='Email da empresa',
        required=False,
        error_messages={
            'invalid': 'O campo Email da empresa deve conter um email válido.'
        }
    )

    empresa_site = forms.URLField(
        label='Site da empresa',
        required=True,
        error_messages={
            'required': 'O campo Site da empresa é obrigatório.',
            'invalid': 'O campo Site da empresa deve conter um endereço web válido.'
        }
    )

    empresa_telefone_celular = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
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
        widget=forms.TextInput(attrs={'type': 'tel'}),
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
        required=True,
        max_length=50,
        error_messages={
            'required': 'O campo Título do cargo é obrigatório.',
            'max_length': 'O campo Título do cargo pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    cargo_descricao = forms.CharField(
        widget=forms.Textarea, label='Descrição do cargo',
        required=False
    )

    site_referencia = forms.URLField(
        label='Site de referência',
        required=True,
        error_messages={
            'required': 'O campo Site de referência é obrigatório.',
            'invalid': 'O campo Site de referência deve conter um endereço web válido.'
        }
    )

    data_hora_entrevista = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime'}, format='%d/%m/%Y %H:%M'),
        label='Data e hora da entrevista',
        required=False,
        error_messages={
            'invalid': 'O campo Data e hora da entrevista deve conter uma data e horário válidos. Ex.: dd/mm/YYYY HH:ii'
        }
    )