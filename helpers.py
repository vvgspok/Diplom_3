import random
import string
from data import domain_name

def generation_mail():
    symbols = string.ascii_lowercase
    user_name = ''.join(random.choice(symbols) for _ in range(10))
    return f"{user_name}@{random.choice(domain_name)}"

def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(8))
    return random_string