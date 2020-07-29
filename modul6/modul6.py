# generator

my_list = [1, 2, 3]
my_gen = (e for e in my_list)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# print(next(my_gen))

def my_new_gen(my_new_list):
    for element in my_new_list:
        if element > 2:
            yield element + 3
            continue
        yield element * 3


gen1 = my_new_gen(my_list)
print(type(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


# print(next(gen1))

def factorial_to_x(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
        yield result


gen2 = factorial_to_x(5)
for _ in range(5):
    print(next(gen2))

print('''new gen''')


def my_new_gen2(y):
    result = [y]
    for _ in range(y):
        new_result = result * 100
        for i in new_result:
            result.append(i)
            yield result


gen3 = my_new_gen2(100)
for _ in range(3):
    next(gen3)


def prime(limit_inf, limit_sup):
    for i in range(limit_inf, limit_sup):
        for j in range(2, i // 2):
            if i % j == 0:
                break
        else:
            yield i


# start = time.time()
# prime_gen = prime(10000, 30000)
# for i in range(2010):
#     next(prime_gen)
# print(next(prime_gen))
# stop = time.time()
# print(stop - start)

# Any function and all function
var1 = any([0, 1, 2, 3])  # or
print(var1)
var2 = all([0, 1, 2, 3])  # and
print(var2)

# iterators
iter_obj = iter([1, 2, 3])
print(type(iter_obj))
print(type(iter_obj.__iter__()))
for i in iter_obj:
    print(i)


class MyIterator():
    my_data = [1, 2, 3]

    # def __str__(self):
    #     print('I am an iterator')
    #
    # def __repr__(self):
    #     print('I am an iterator')

    def __iter__(self):
        return self

    def __next__(self):
        if not len(my_list):
            raise StopIteration
        return my_list.pop(0)


my_iter = MyIterator()
print(type(my_iter))
print(type(my_iter.__iter__()))
for i in my_iter:
    print(i)


# improved iterator

class MyIterator():
    my_data = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.my_data
        self.my_data = x + 1
        if x < 10:
            return x
        raise StopIteration


my_iter1 = MyIterator()
for i in my_iter1:
    print(i)

# example
print('=========================')
string1 = 'abc'
obj1 = string1.__iter__()

for i in string1:
    print(i)

for i in string1:
    print(i)

print('=========================')


class MyIterableObject():
    def __iter__(self):
        return MyIterator()

    def my_test(self):
        print('+++', '+0+', '+++', sep='\n')


my_iterable_object = MyIterableObject()
my_iterable_object.my_test()
for i in my_iterable_object:
    print(i)
for i in my_iterable_object:
    print(i)


class Prime():
    def __init__(self, lim_inf, lim_sup):
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.partial_res = None
        self.var = list(range(self.lim_inf, self.lim_sup))

    def __iter__(self):
        return self

    def __next__(self):
        self.partial_res = self.var.pop(0)
        for j in range(2, self.partial_res // 2):
            if self.partial_res % j == 0:
                self.__next__()
        else:
            return self.partial_res


var4 = Prime(128, 256)
print(next(var4))
