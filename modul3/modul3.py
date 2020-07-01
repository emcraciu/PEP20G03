# If statement

def return_true():
    return 1


def return_false():
    return ''


if return_true():
    print('True')

if return_false():
    print('if executed')
else:
    print('else execute')

if return_false():
    pass
elif return_true():
    print('elif execute')
else:
    print('else execute')

# if assigment operator
var1 = 'a' if 3 < 1 else return_false()
print(var1)


def comp_numar():
    numar = int(input("da numarul: "))
    if numar <= 3:
        print("mic")
    elif numar >= 3 and numar < 5:
        print("egal")
    else:
        print("mare")


# comp_numar()


# loops

tuple1 = (1, 2, 3)
iterable = tuple1.__iter__()
print(iterable.__next__())
print(next(iterable))
print(next(iterable))
# print(next(iterabil))
print(iterable)

for var in tuple1:
    print(var)
    if var == 2:
        break
else:
    print('end of for')


def found_a():
    var = input("input: ")
    for letter in var:
        if letter == 'a':
            print('exista: a')
            break
    else:
        print('nu exista: a')


# found_a()

while True:
    print('i am lost')
    break

# while with counter

counter = 0
while counter < 5:
    print('i am lost')
    if counter == 4:
        break
    counter += 1
else:
    print('condition not True')


def a_in_string():
    user_text = input('write string: ')
    for letter in user_text:
        if letter == 'a':
            print('we have: a')
            return False
    else:
        return True


def find_a():
    while a_in_string():
        pass


# find_a()


# instance

print(isinstance('a', str))

# Recursive function
tuple_bool = (((True,),),)


# return the first object bool object or None
# will not work with multiple tuples
def find_bool(tuple_object, level=0):
    for var in tuple_object:
        print('object at level {}: {}'.format(level, var))
        if isinstance(var, tuple):
            return find_bool(var, level + 1)
        if isinstance(var, bool):
            return var


print(find_bool(tuple_bool))

tuple_complex = (1, 'a', ('b', ('c', 3), 1 + 1, (0 + 1j, 'z')))


# returns first complex number or False
# will not work with multiple tuples
def find_complex(tuple_object, level=0):
    for var in tuple_object:
        print('object at level {}: {}'.format(level, var))
        if isinstance(var, complex):
            return var
        if isinstance(var, tuple):
            result = find_complex(var, level + 1)
            if result is not False:
                return result
    else:
        return False


print(find_complex(tuple_complex))
