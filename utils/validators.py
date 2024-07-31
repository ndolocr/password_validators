class Validator:
    
    "Function to check if password has more than 8 characters"
    def long_enough(password):
        """Password must be atleast 8 characters long"""
        check = len(password)> 8
        if check:
            return check
        else:
            return Validator.long_enough.__doc__