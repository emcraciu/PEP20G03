# pentru a intelege mai bine recursivitatea va recomand https://realpython.com/python-thinking-recursively/ si
# https://www.python-course.eu/python3_recursive_functions.php

# 40P
# dupa ce ati citit articolul vreau sa incercati sa calculati recursiv seria 1^2+2^2+3^2...
# folosind o functie scrisa de voi ce primeste ca argument doar numarul de ordine
# exemplu de logica 1^2+2^2 este 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    pass
    # <your code here>

print(sum_of_square(10))

# 30P
# sctrieti o functie care calculeaza n! fara sa folositi recursivitatea

def factorial(n:int):
    pass
    # <your code here>

print(factorial(10))

# 30P
# creati o functie care primeste un string ca argument si returneaza un tuple aplicand urmatoarele actiuni:
# - string-ul initial este impartit dupa primul spatiu si in contiunuare vom modifica doar ce este dupa spatiu
# - tate caracterele care nu sunt litere mici vor fi inlocutite cu _
# tuple-ul returnat contine prima parte de text (pana la primul spatiu) si partea modificata
# exemplu (1234567A Text de te5t > (1234567A, _ext_de_te_t))

def process_text(text: str):
    pass
    # <your code here>

print(process_text('1234567a Text de te5t'))

# Temele trebuie predate pana la examen