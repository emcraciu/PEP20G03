from random import randint

from communicator import MySecret
from utils.prime import prime


class Client(MySecret):
    def __init__(self):
        primes = prime(128, 256)
        number_of_primes = len(primes)
        rand_element1 = randint(0, number_of_primes - 2)
        rand_element2 = randint(rand_element1 + 1, number_of_primes - 1)

        self.prime = primes[rand_element1]
        self.base = primes[rand_element2]

