import re 
import string


class RegisterValidator:
    
    def validate_email(self, email):
        pattern = re.compile(r'\w+@\w+\.\w+')

        result = pattern.search(email)

        if result is None:
            return False
       
        return True

    def __check_if_at_least_one_character_matches(self, string1, string2):
        for character in string1:
            if character in string2:
                return True

        return False

    def validate_password(self, password):
        
        requirements = (
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits,
            string.punctuation
        )
        
        needed_requirements = 5

        requirements_counter = 0
        
        if 5 <= len(password) <= 20:
            requirements_counter += 1

        for requirement in requirements:
            if self.__check_if_at_least_one_character_matches(password, requirement):
                requirements_counter += 1
    
        return requirements_counter == needed_requirements  
            