# validators.py

import re
from django.core.exceptions import ValidationError

def validate_cameroonian_phone_number(value):
    cameroon_number_regex = re.compile(r'^(\+237|237)?[2368]\d{8}$')
    if not cameroon_number_regex.match(value):
        raise ValidationError(
            f'{value} is not a valid Cameroonian phone number. A valid number should start with +237, 237, or 6/2 followed by 8 digits.'
        )

