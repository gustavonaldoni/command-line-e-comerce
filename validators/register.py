import re 


class RegisterValidator:
    
    def validate_email(self, email):
        pattern = re.compile(r'\w+@\w+\.\w+')

        result = pattern.search(email)

        if result is None:
            return False
       
        return True
