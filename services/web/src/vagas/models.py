from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from typing import Any
import re
from datetime import datetime
from vagas.validators import is_equal_to_or_later_than_current_datetime

class TelefoneField(models.CharField):
    
    def get_prep_value(self, value: Any) -> Any:
        regex = re.compile('\D+')

        return regex.sub('', str(value))
    
    def from_db_value(self, value: Any, expression, connection):
        if value:
            phone_regex = re.compile(r'^(\d{2})(\d{1,})(\d{4})$')
            p1, p2, p3 = phone_regex.search(value).groups()
            
            return f'({p1}) {p2}-{p3}'
        
        return value

class Vaga(models.Model):
    """A job opportunity model."""

    class Status(models.TextChoices):
        APPLIED = 'C', 'Candidatado'
        WAITING = 'W', 'Aguardando retorno'
        INTERVIEW_SCHEDULED = 'S', 'Entrevista agendada'
        REJECTED = 'R', 'Rejeitado'

    empresa_nome = models.CharField(
        max_length=100,
        blank=False,
        error_messages={
            'blank': 'O campo Nome da empresa é obrigatório.',
            'max_length': 'O campo Nome da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_endereco = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        error_messages={
            'max_length': 'O campo Endereço da empresa pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    empresa_email = models.EmailField(
        null=False,
        blank=True,
        error_messages={
            'invalid': 'O campo Email da empresa deve conter um email válido.'
        }
    )
    
    empresa_site = models.URLField(
        null=False,
        blank=False,
        error_messages={
            'blank': 'O campo Site da empresa é obrigatório.',
            'invalid': 'O campo Site da empresa deve conter um endereço web válido.'
        }
    )
    empresa_telefone_celular = TelefoneField(
        max_length=15,
        null=False,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\(\d{2}\) 9\d{4}-\d{4}$',
            message='O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999',
            code='invalid'
        )]
    )

    empresa_telefone_comercial = TelefoneField(
        max_length=14,
        null=False,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\(\d{2}\) \d{4}-\d{4}$',
            message='O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999',
            code='invalid'
        )]
    )

    cargo_titulo = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        error_messages={
            'blank': 'O campo Título do cargo é obrigatório.',
            'max_length': 'O campo Título do cargo pode conter no máximo %(limit_value)s caracteres.'
        }
    )

    cargo_descricao = models.TextField(
        null=False,
        blank=True
    )

    site_referencia = models.URLField(
        null=False,
        blank=False,
        error_messages={
            'blank': 'O campo Site de referência é obrigatório.',
            'invalid': 'O campo Site de referência deve conter um endereço web válido.'
        }
    )
    
    data_hora_entrevista = models.DateTimeField(
        null=True,
        blank=True,
        error_messages={
            'invalid': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos',
            'invalid_datetime': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos'
        }
    )

    situacao = models.CharField(
        null=False,
        blank=False,
        max_length=1,
        choices=Status.choices,
        default=Status.APPLIED,
        error_messages={
            'blank': 'O campo Situação é obrigatório.',
            'invalid_choice': 'O campo Situação contém um valor inválido.',
        },
    )

    data_hora_cadastro = models.DateTimeField(auto_now_add=True)
    
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Return user-friendly representation of this model.

        :return: str
        """
        return self.empresa_nome
    
    def get_absolute_url(self) -> str:
        """
        Return the canonical URL for this model instance.

        :return: str
        """
        return f'/oportunidades/{str(self.id)}'
    
    def clean(self):
        if self.situacao == self.Status.INTERVIEW_SCHEDULED and self.data_hora_entrevista is None:
            raise ValidationError({
                'data_hora_entrevista': ValidationError(
                    "O campo Data e o horário da entrevista deve ser preenchido caso a situação do cadastro seja 'Entrevista agendada'.",
                    code='required'
                )
            })
        
        if isinstance(self.data_hora_entrevista, datetime):
        
            if self.situacao == self.Status.APPLIED:
                raise ValidationError({
                    'data_hora_entrevista': ValidationError(
                        "O campo Data e horário da entrevista deve estar vazio caso a situação do cadastro seja 'Candidatado'.",
                        code='invalid_datetime'
                    )
                })
        
            if self.pk is None and not is_equal_to_or_later_than_current_datetime(self.data_hora_entrevista):
                raise ValidationError({
                    'data_hora_entrevista': ValidationError(
                        'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.',
                        code='invalid_datetime'
                    )
                })
