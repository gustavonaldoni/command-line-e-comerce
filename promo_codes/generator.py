import string
import random

class PromoCodeGenerator:
    
    all_upper = string.ascii_uppercase
    all_digits = string.digits

    def __choose_character_type(self):
        available_types = (self.all_upper, self.all_digits)
        chosen_type = random.choice(available_types)

        return chosen_type

    def generate_code(self, length: int) -> str:
        code = ''

        for _ in range(length):
            character = random.choice(self.__choose_character_type())
            code += character

        return code

    def generate_discount_percentage(self, discount_range: tuple) -> int:
        min_value, max_value = discount_range
        possibilities = [number for number in range(min_value, max_value + 1) if number % 5 == 0]
        
        discount_percentage = random.choice(possibilities)

        return discount_percentage


if __name__ == '__main__':
    gen = PromoCodeGenerator()

    print(gen.generate_code(5), f'{gen.generate_discount_percentage((5, 30))}%')
    