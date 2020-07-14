# lists
var1 = ('1', '2')
my_list = [1, 2, 3, 'a', var1]
print(my_list)

# mutable object
print(id(my_list))
my_list.append('z')
print(id(my_list))
print(my_list)

# copy of fist changes ID
my_new_list = my_list[:]
print(id(my_new_list))
print(my_new_list)

# list operations
my_new_list.remove(1)
print(my_new_list)
print(my_new_list.index('a'))
print(my_new_list.count('z'))
my_new_list.extend('abc')
print(my_new_list)
returned_object = my_new_list.pop(0)
print(returned_object)
print(my_new_list)
my_new_list.insert(3, 'x')
print(my_new_list)

# ex.
list1 = [1, 2, 3, 4, 'abc']
# print (reverse list)
# print (int objects)


# print(list1.pop(100))

# recap
var1 = 1 if True else 2

# list comprehension

list2 = [obj for obj in 'my string']
print(list2)

list3 = [obj for obj in 'my string' if obj != ' ']
print(list3)

# generators
generator = (obj for obj in 'my string')
print(type(generator))
print(next(generator))

for letter in generator:
    print(letter)
print('#' * 80)

# lenght of objects
print(len(list2))
# print(len(generator))

# long_list = [obj for obj in range(100000000)]
# print(len(long_list))
# long_gen = (obj for obj in range(100000000))


# exceptions

try:
    a = 1 / 0
except:
    print('I can`t do this')
    a = 10000000000000000000000000000000000000000000000000000000000
    raise


try:
    a = open('x')
except ZeroDivisionError:
    print('I can`t do this')
    a = 10000000000000000000000000000000000000000000000000000000000

print(a)

print(1 / 3)

# exercitiu1
list_to_flatten = [[1, 2, 3], ['a', 'b', 'c'], [(), (), ()]]


# def flatten_list(input_list, return_list=[]):
#     for inner_object in input_list:
#         if isinstance(inner_object, list):
#             flatten_list(inner_object, return_list)
#         else:
#             return_list.append(inner_object)
#     return return_list


def flatten_list(input_list):
    return_list = []
    for inner_object in input_list:
        if isinstance(inner_object, list):
            return_list.extend(flatten_list(inner_object))
        else:
            return_list.append(inner_object)
    return return_list


print(flatten_list(list_to_flatten))

list1 = []
list2 = []
print(id(list1))
print(id(list2))



myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

s = []
for i in myList[:]:
    if i not in s:
        s.append(i)
    else:
        myList.remove(i)

print("The list with unique elements only:")
print(myList)

list_to_iter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_obj = list_to_iter.__iter__()
print(next(iter_obj))
print(list_to_iter)
list_to_iter.pop(0)
print(list_to_iter)
print(next(iter_obj))

# dictionary
dict1 = {'key1': 1, 'key2': 2}
# ''.__hash__()

for obj in dict1:
    print(type(obj))
    print(obj)

# keys
print(type(dict1.keys()))
for obj in dict1.keys():
    print(type(obj))
    print(obj)

for obj in dict1.values():
    print(type(obj))
    print(obj)

for key, value in dict1.items():
    print(key)
    print(value)

# exerciciu magazin

magazin1 = {'lego': 50, 'HotWheels': 60, 'Barbie': 30, "jucarie1": 30}
magazin2 = {'lego': 60, 'HotWheels': 55, 'Barbie': 25, "jucarie2": 31}
magazin3 = {'lego': 55, 'HotWheels': 70, 'Barbie': 14, "jucarie3": 32}
lista_de_cumparaturi = {'lego': 1, 'HotWheels': 2, 'Barbie': 3}
DEFAULT_SHOPS = {}
from utils.best_buy import DEFAULT_SHOPS as shops
from utils.best_buy import best_buy

# from utils.best_buy import *
# import utils.best_buy

print(best_buy(*shops, to_buy=lista_de_cumparaturi))

# sets

set1 = {1, 2, 4, 4}
set2 = {1, 2, 3}
print(type(set1))
print(set1)
result = set1.intersection(set2)
print(result)
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

# pinball test
from utils.pinnball_test import pinball_test, DEFAULT_TEST_DATA as test_data
print(pinball_test(test_data))



