from .utilities import get_random_number

class User:
    def __init__(self, first_name: str):
        self.first_name = first_name
        self.favorite_number = get_random_number()

    def get_greeting_string(self):
        return f'Hello! My name is {self.first_name} and my favorite number is {self.favorite_number}.'
