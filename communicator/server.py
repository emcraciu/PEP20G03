import time
from random import randint
from socket import socket
from threading import Thread

from communicator import MySecret
from utils.prime import prime


class Server(MySecret):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        primes = prime(128, 256)
        number_of_primes = len(primes) - 1
        rand_element1 = randint(0, number_of_primes - 1)
        rand_element2 = randint(rand_element1, number_of_primes - 1)

        self.prime = primes[rand_element1]
        self.base = primes[rand_element2]
        self.messages = None


    def start(self):
        """Start communication server to listen for incoming connections

        :return: None
        """
        self.socket = socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.process = Thread(target=self.receive_message,
                              args=(self.messages,))
        self.process.start()
        #self.__client_key_exchange()

    def stop(self):
        """Stop communication server
        :return:
        """
        self.process.join()


    def receive_message(self, messages):
        """Connect to socket and listen for incoming key exchange and message

        :param messages: list to
        :return:
        """
        connection, addr = self.socket.accept()
        print('Server accepted connection:', connection, addr)
        time.sleep(10)
        # with connection:
        #     self.__server_key_exchange(connection)
        #     encrypted_message = str(connection.recv(4096), encoding='UTF-8')
        # message = decrypt(encrypted_message, self._Communicator__shared_secret)
        # messages.append((addr, message))