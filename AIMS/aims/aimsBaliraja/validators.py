from django.core.exceptions import ValidationError


def validate_mob_no(value):
    if value=="":
        raise ValidationError('This field cannot be empty')
    return value
