import random
from chalicelib.data import COMPLIMENTS


def get_random_compliment():
    return random.choice(COMPLIMENTS) + "\nAtte. Ing. Brayan Altamar"
