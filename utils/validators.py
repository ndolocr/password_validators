import string
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
    
    @staticmethod
    def has_lowercase(password):
        """Password must contain a lowercase letter"""
        check = len(set(string.ascii_lowercase).intersection(password)) > 0
        if check:
            return check
        else:
            return Validator.has_lowercase.__doc__
        
    @staticmethod
    def has_uppercase(password):
        """Password must contain an uppercase letter"""
        check = len(set(string.ascii_uppercase).intersection(password)) > 0
        if check:
            return check
        else:
            return Validator.has_uppercase.__doc__
        
    @staticmethod
    def has_numeric(password):
        """Password must contain a digit"""
        check = len(set(string.digits).intersection(password)) > 0
        if check:
            return check
        else:
            return Validator.has_numeric.__doc__
    
    @staticmethod
    def has_special(password):
        """Password must contain a special character"""
        check = len(set(string.punctuation).intersection(password)) > 0
        if check:
            return check
        else:
            return Validator.has_special.__doc__