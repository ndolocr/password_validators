from utils.validators import Validator

password_validators = [
    Validator.long_enough
]

def validate_password(password):
    for validator in password_validators:
        validated_psw = validator(password)
        if isinstance(validator, str):
            return validator
    return True