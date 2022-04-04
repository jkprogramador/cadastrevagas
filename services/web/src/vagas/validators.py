from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

def is_equal_to_or_later_than_current_datetime(value: datetime) -> bool:
    """
    Check whether the given datetime is equal to or later than the current datetime.

    :param value: A datetime object

    :type value: datetime

    :returns: True if value is equal to or later than the current datetime; False otherwise.

    :rtype: bool
    """
    now = timezone.localtime().replace(second=0, microsecond=0)
    value = value.replace(second=0, microsecond=0)

    return value >= now

def validate_data_hora_entrevista(value) -> None:

    if not is_equal_to_or_later_than_current_datetime(value):
        raise ValidationError(
            'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.',
            code='invalid_datetime'
        )