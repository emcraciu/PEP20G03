color = 'green'
print(color)
color = 'red'
print(color)


# class
class Car(object):
    """My first class"""

    def __init__(self):
        self.color = 'red'

    def __str__(self):
        return 'this is the class string'

    def paint_car(self):
        self.color = 'green'


my_car = Car()
print(type(my_car))
print(my_car.__doc__)
print(my_car.color)
print(my_car.__str__())
print(my_car.paint_car())
print(my_car.color)


# instance variables
class Animal():
    pass


class Wolf(Animal):

    def __init__(self):
        print('wolf')
        self.has_pack = True
        print('###', self.breed)

    def bark(self):
        print('ham')


class Dogs(Wolf):

    def __init__(self, breed):  # overload
        print('dog')
        self.breed = breed
        super().__init__()


dog = Dogs(breed='Husky')
dog.bark()
print(dog.breed)
print(dog.has_pack)

# class variables

data = 1


def test_data():
    if data:
        print('We have data')


test_data()


class SportCars:
    color = 'white'

    def __init__(self, color):
        print(color)
        print(self.color)
        self.color = color


s_car = SportCars('blue')

print('##############')


# class variable reference issue
class Fruits:
    colors = ['white']

    def __init__(self):
        print(id(self.colors))


fruit1 = Fruits()
print(id(Fruits.colors))
fruit1.colors.append('pink')
print(id(fruit1.colors))
print(Fruits.colors)
fruit2 = Fruits()
print(fruit2.colors)

import communicator

text = 'text to encode'
secret = communicator.MySecret()
encoded_text = secret.encode(text)
print(encoded_text)
print(len(encoded_text))
secret2 = communicator.MySecret()
decoded_text = secret2.decode(encoded_text)
print(decoded_text)
print(len(decoded_text))

### variables (global, non-local, local)
print('###############')
global_var = 'a'


def func1():
    global global_var
    global_var = 'b'
    local_var = 'c'

    def func2():
        nonlocal local_var
        local_var = 'd'
        print('non-local in func2: ', local_var)

    func2()
    print('local in func1: ', local_var)
    print('global in func1: ', global_var)


func1()
print('after function: ', global_var)


class A():
    def method_a(self):
        print('a')


class B(A):
    def method_a(self):
        print('b')

    def method_b(self):
        print('b_1')


class C(B, A):
    pass
    # def method_a(self):
    #     print('c')


c = C()
c.method_a()
c.method_b()

from communicator import Client

client = Client()
print(client.prime, client.base)
from communicator import Server

server = Server()
print(server.prime, server.base)

a = 0


class OtherMathError(ArithmeticError):
    ex_info = 'math data'

    def __init__(self, *args, **kwargs):
        print(args)


try:
    if a:
        raise OtherMathError('This is my math error')
    else:
        0 / 0
except OtherMathError as error:
    print(error.ex_info)
    print('This is something else')
except ZeroDivisionError as e:
    print('Not a good number')
except ArithmeticError:
    print('other math error')
except:
    print(0)


# lambda functions
def var1(a, b):
    return a + b


var1 = lambda a, b: a + b


print(var1(1, 2))
print(type(var1))


def math_calc(func1, number):
    return (3 * func1(number) + 1) ** (1 / 2)


print(math_calc(lambda x: x * 3, 2))
