from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_data_hora_entrevista(value):
    now = timezone.localtime().replace(second=0, microsecond=0)
    data_hora_entrevista = value.replace(second=0, microsecond=0)
    
    if data_hora_entrevista < now:
        raise ValidationError([{
            'data_hora_entrevista': 'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.'
        }])