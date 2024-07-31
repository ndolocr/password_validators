from utils.validators import Validator

password_validators = [
    Validator.long_enough,
    Validator.short_enough,
    Validator.has_lowercase,
    Validator.has_uppercase,
]

def validate_password(password):
    for test_fn in password_validators:
        test = test_fn(password)
        if isinstance(test, str):
            return test
    return True