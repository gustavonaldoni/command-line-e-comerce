from register import RegisterValidator


class TestRegisterValidator:

    validator = RegisterValidator()

    def test_validate_email(self):
        examples = {
            'a@a.com' : True,
            'aaaaa@gmail.com' : True,
            '1233@gmail.com' : True,
            'gutgfuy12345@hotmail.com' : True,
            'aaaaa@123.com' : True,
            'aaaaa@gmail.com.br' : True,
            'trewtrew' : False
        }

        for email, result in examples.items():
            assert self.validator.validate_email(email) == result, print(f'ERROR ON -> {email}')

    def test_validate_password(self):

        examples = {
            'Aaaa9*' : True,
            'Aggsgf4536*(' : True,
            'huHu489398***' : True,
            'aaa' : False,
            'Ab6*' : False,
            'fdhskagdfgkjhdsaA' : False,
            'passworD' : False,
            'passworD123' : False,
            '123456' : False
        }

        for password, result in examples.items():
            assert self.validator.validate_password(password) == result, print(f'ERROR ON -> {password}')