print('# Integers')
int1 = 1
print(type(int1))
print(dir(int1))

# # octal values
# 0,1,2,3,4,5,6,7,10,11..
#
# # binary values
# 0,1,10,11,100..
#
# # hex values
# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10..1F..,
# 0-F = 0000-1111
# 00-FF = 00000000-11111111

# write number in hex
hex1 = 0x1f
print(hex1)

# write number in octal
oct1 = 0o12
print(oct1)

# write number in binary
bin1 = 0b11
print(bin1)

# write number with exponent
exp1 = 3e4
print(exp1)
print(type(exp1))

print('# Arithmetic operators')
# sum
sum1 = hex1 + oct1
print(sum1)
print(hex1.__add__(oct1))
print(oct1.__add__(hex1))

# division
div1 = 1 / 3
print(div1)
div2 = (1).__truediv__(3)
print(div2)

# power of
pow1 = 2 ** 2
print(pow1)
pow2 = pow(2, 3)
print(pow2)

# calculate
a = 3
b = 4
c = 5
x = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
print(x)

print('# Float and Complex')
int1 = 1
float1 = 1.0
complex1 = 0.2 + 0.1j

sum_float_int = float1 + int1 + complex1
print(sum_float_int)

print('# Bool')
obj1 = True
obj2 = False
obj3 = True

print(id(obj1))
print(id(obj2))
print(id(obj3))

# print bool object
print(type(True))
print(type(str(True)))
print(type(True.__str__()))

# unary operation
not1 = not True
print(not1)

# binary operation
and1 = False and True or True
print(and1)

# convert to bool
print(bool(0))
print(bool(0.0))
print(bool(0.0 + 0.0j))
print(bool(''))
print(bool(False))
print(''.__len__().__bool__())
print((0).__bool__())

# None type object
none = None

print('# Strings')
string1 = r'a' \
          r'b' \
          r'c'
string2 = """a
             b
             c"""
print(string1)
print(string2)

# adding string
text = string1 + string2
print(string1 + string2)
print(string1.__add__(string2))
print(text * 2)
print(text.__mul__(2))

# order of operations
print(string1 + string2 * 3)

# slice
text = "Hello {}{replace} World"
print(text[0:5:2])
print(text[-5:])
print(text[:5:-1])

# string methods
format_text = text.format('abc', replace='abc')
print(format_text)

join_text = ' ! '.join([text, text])
print(join_text)

nr_of_char = len(text)
print(nr_of_char)

text1 = "/text/"
text2 = text1
text3 = text2[:]  # not true all the time
print(text1 == text3)
print(text1 is text3)
print(id(text1))
print(id(text2))
print(id(text3))

# # is and ==
# print(obj1 is obj3)
# print(obj1 == obj3)

# Operators
greater = 2 >= 2
print(greater)
print(type(greater))

equal = 2 != 2
print(equal)

# div_by_0 = 0/0

# assignment operators
a = 1
a = a + 1
print(a)

a = 1
a += 1
print(a)

result = 1 < 1.1
print(result)

# compare strings
and_str = "a" and "b"
print(and_str)
print(and_str == "b")

and_str = "a" or "b"
print(and_str)
print(and_str == "b")

# convert to int
result = True + False + 1
print(result)

# switch variables
var1 = 1
var2 = 2
var1, var2 = var2, var1
print(var1)
print(var2)


# functions:
def func1():
    print('hello world')
    return None


print(type(func1))
print(type(func1()))
func1.__call__()


def func2():
    return 'hello world 2'


result = func2()
print(result)


def func3(text1, text2):
    print(text1, text2, sep='__')


func3('hello', 'world')


def func4(text1, text2, x=None, y='\n'):
    print(text1, text2, sep=x, end=y)


func4('hello', 'world')
func4('hello', 'world', ' x ')
func4('hello', 'world', y=' y \n')

print('# Tuple')
tuple1 = (1, 1, 3)
print(type(tuple1))
tuple2 = '1',
tuple3 = tuple2 + tuple1
print(tuple3)
tuple4 = tuple2 * 4
print(tuple4)

print('# condense arguments')


def func4(*args, x=None, y='\n'):
    print(type(args))
    print(len(args))
    print(args[0], args[1], sep=x, end=y)


func4('hello', 'world', 'terra', y=' y \n')


def func5(*args, **kwargs):
    print(type(kwargs))
    print(len(kwargs))
    print(args[0], args[1], sep=kwargs['x'], end=kwargs['y'])


func5('hello', 'world', 'terra', y='y \n', x='__')

# homework function

# bitwise operations
nr_bin = bin(100)
print(nr_bin)
and_bits = 1 & 2
print(and_bits)
or_bits = 10 | -10
print(or_bits)
print(bin(-0))

# encrypt using XOR
message = ord("A")
key = ord("c")
encrypted = message ^ key
print(chr(encrypted))
decrypted = encrypted ^ key
print(chr(decrypted))


def crypt(text, key):
    return chr(ord(text[0]) ^ key) + \
           chr(ord(text[1]) ^ key) + \
           chr(ord(text[2]) ^ key)


print(crypt('abc', 7))
