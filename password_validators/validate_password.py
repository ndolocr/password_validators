from utils.validators import Validator

password_validators = [
    Validator.long_enough,
    Validator.short_enough,
]

def validate_password(password):
    for test_fn in password_validators:
        test = test_fn(password)
        if isinstance(test, str):
            return test
    return True