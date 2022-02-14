from django.db import models
from django.utils import timezone
from datetime import datetime as dt
from typing import Any
import re

class DataHoraField(models.DateTimeField):
    def get_prep_value(self, value: Any) -> Any:
        return timezone.make_aware(dt.strptime(value, "%d/%m/%Y %H:%M"))

class TelefoneField(models.CharField):
    def get_prep_value(self, value: Any) -> Any:
        regex = re.compile('\D+')
        return regex.sub('', str(value))

class Vaga(models.Model):
    """A job opportunity model."""

    empresa_nome = models.CharField(max_length=100)
    empresa_endereco = models.CharField(max_length=200)
    empresa_email = models.EmailField()
    empresa_site = models.URLField()
    empresa_telefone_celular = TelefoneField(max_length=11)
    empresa_telefone_comercial = TelefoneField(max_length=10)
    cargo_titulo = models.CharField(max_length=50)
    cargo_descricao = models.TextField()
    site_referencia = models.URLField()
    data_hora_entrevista = DataHoraField()
    data_hora_cadastro = models.DateTimeField(auto_now_add=True)

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
