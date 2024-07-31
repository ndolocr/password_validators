class Validator:
    
    "Function to check if password has more than 8 characters"
    @staticmethod
    def long_enough(password):
        """Password must be atleast 8 characters long"""
        check = len(password) >= 8

        if check:
            return check        
        return Validator.long_enough.__doc__
        
    @staticmethod
    def short_enough(password):
        """Password cannot be more than 32 characters"""
        check = len(password) <=32
        if check:
            return check
        return Validator.short_enough.__doc__