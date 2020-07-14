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


