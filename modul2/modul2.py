# Integers

integ1 = 1
print(type(integ1))
print(dir(integ1))

# # octal values
# 0,1,2,3,4,5,6,7,10,11
#
# # binary values
# 0,1,10,11,100
#
# # hex values
# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10..1F,
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

# operators and methods
sum1 = hex1 + oct1
print(sum1)
print(hex1.__add__(oct1))
print(oct1.__add__(hex1))

# division
div1 = 1 / 3
div1 = (1).__truediv__(3)
print(div1)

# exponent
pow1 = 2**2
print(pow1)
pow2 = pow(2, 3)
print(pow2)

# calculate
a = 3
b = 4
c = 5
x = (-b + (b**2 - 4 * a * c)**(1/2)) / (2 * a)
print(x)

# float and complex
int1 = 1
float1 = 1.0
complex1 = 0.2 + 0.1j

sum_float_int = float1 + int1 + complex1
print(sum_float_int)

# Bool object
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
print(bool(0.0+0.0j))
print(bool(''))
print(bool(False))
print(''.__len__().__bool__())
print((0).__bool__())

# None type object
none = None


# Strings
string1 = r'ab\n' \
          r'c'
string2 = """a
             b
             c"""
# print(string1)
# print(string2)

# adding string

string1 = 'x'
string2 = 'y'
string3 = 'z'
text = string1 + string2
print(string1 + string2)
print(string1.__add__(string2))
print(text * 2)
print(text.__mul__(2))

# order of operations
print(string1+string2*3)

# slice
text = "Hello {}{replace} World"
print(text[0:5:2])
print(text[-5:])

# string methods
formated_text = text.format('abc', replace='abc')
print(formated_text)

join_text = ' ! '.join([text, text])
print(join_text)

nr_of_char = len(text)
print(nr_of_char)

text1 = 'my_text'
text2 = text1
text3 = text1[:]
print(text1 == text3)
print(text1 is text3)
print(id(text1))
print(id(text2))
print(id(text3))






# # is and ==
# print(obj1 is obj3)
# print(obj1 == obj3)
#
