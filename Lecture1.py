# CIS 192 Fall 2016
# Lecture 1: Introduction
# Author: Harry Smith
# Date: January 18, 2016

### Intro to Python: Primitive Datatypes and Operators ###

# Names and binding. No declared types.
from math import *  # import everything!!
from math import pow  # import just 'pow' -- now we don't need to say 'math.pow'
import math as m
import math
x = 1
y = x
x = 'a'
print('x: {} y: {}'.format(x, y))

# Objects
x = 1
id(x)  # => address of the object the name x binds to in memory
dir(x)  # => valid attributes of the object
type(x)  # => <class 'int'>
help(int)  # => overview of different properties/methods of class of that object

# lists and tuples: they hold stuff just like arrays do.
# we'll learn more about these below!
y = [1, 2]
z = (1, 2)
print('type y: {} type z: {}'.format(type(y), type(z)))

# `is`: referential equality. do x and y point to the same object?
# `==`: structural equality: are x and y equal based on object's __eq__ method?
[] == []  # => True
[] is []  # => False

# Types
isinstance(5, int)  # => True

### Integers/Floats/Math ###

1 + 1  # => 2
10 - 3  # => 7
6 * 4  # => 24
35 / 5  # => 7
5 / 2  # => 2.5 (In python 2.7, this would be 2...)

# Floor division
5 // 2  # => 2

# Mod operator
10 % 3  # => 1

# Exponentiation (x to the yth power)
2 ** 4  # => 16

# Enforce precendence with parenthesis
(1 + 3) * 2  # => 8

# Floats
1.0
4 * 2.5  # => 10.0
int(2.0)  # => 2

x = 10
x += 1
x  # => 11

# Complex Numbers
3+4j
2.0-3.4j

x = 3j
x += 1
x  # => 1+3j

x.imag  # => 3j
x.real  # => 1

### Booleans ###

True  # => True
False  # => False

# Python booleans and their operators are very readable.
# Use 'and' instead of '&&', 'or' instead of '||', 'not' instead of '!'
True or False  # => True
False and True  # => False
not True  # => False

# Any object can be tested for truth value for use in conditionals, or as
# operands of the above Boolean operations.

# None, False, 0, 0.0, and any empty string/sequence/collection is
# considered false. All other values are true.
bool(0)  # => 0

# and, or both return one of their operands, and are short-circuit operators.
0 and 2  # => 0 (because 0 is "falsy")
0 or 3  # => 3
0 or 3 or None  # => 3

### Strings ###

print('Hello World')  # "Hello World!"
'Hello World' == "Hello World"  # => True
dir('Hello World')  # => list of attributes of 'Hello World': [..., 'split', ...]

'hello world'.title()  # => "Hello World"

### Program Flow ###

# Spacing is important -- no curly braces for control flow!
# Please use four spaces per indent in this class.

### Conditionals ###

# Single if
if True:
    print('if')

# if/else
if False:
    print('if')
else:
    print('else')

# 1 or more elifs
if 1 > 2:
    print('if')
elif 'b' < 'a':
    print('elif 1')
elif isinstance(1, int):
    print('elif 2')

### Sequences ###
my_string = 'string'
type(my_string)  # => <class 'str'>
my_tuple = (1, 2, 3)
type(my_tuple)  # => <class 'tuple'>
my_list = [1, 2, 3]
type(my_list)  # => <class 'list'>

# getting first element of a sequence
my_string[0]  # => 's'
my_tuple[0]  # => 1
my_list[0]  # => 1

# lists are mutable
my_list[0] = 5  # OK
# strings, tuples are immutable
my_tuple[0] = 5  # => TypeError
my_string[0] = 'b'  # => TypeError

# `in` and `not in` to check for membership
if 'x' in 'string':
    print('x in')
elif 'ring' in 'string':
    print('ring in')

2 not in (1, 2, 3)  # => False

# len(sequence) gives you its length
len(my_list)  # => 3

### Lists ###
# We'll cover these more in-depth next lecture.
# Lists are similar to ArrayLists in Java

lst = [4, -3.0, 'hi', 17, 'python is awesome']
lst[0]  # => 4
lst.append('hi')

print(lst)

### Ranges ###

print(range(3))  # => range(0, 3)
print(type(range(3)))  # => <class 'range'>

# range([start, ]stop[, step])

print(list(range(3)))  # => [0, 1, 2]

print(list(range(-1, 3)))  # => [-1, 0, 1, 2]
print(list(range(5, 2, -2)))  # => [5, 3]
# Ranges are memory efficent.

### Loops ###

for i in range(3):
    print(i)

for item in lst:
    print(item)

# break
for letter in 'abcd':
    if letter != 'c':
        print(letter)
    else:
        break
else:
    # No break!
    print('else')

# continue and the importance of whitespace
for letter in 'abcd':
    if letter != 'c':
        print(letter)
else:
    print('else')

# while break
i = 0
while i <= 4:
    if i != 3:
        print(i)
    else:
        break
    i += 1
else:
    # No break!
    print('else')

# while continue
i = 0
while i <= 4:
    if i != 3:
        print(i)
    else:
        i += 1
        continue
    i += 1
else:
    print('else')

# falsy conditionals
x = 1
while x:
    print('x is truthy:', x)
    x = 0

print('x is falsy:', x)

# Functions ###


def some_func():
    print('Hello this is some arbitrary function that prints stuff')


some_func()


def plus_2(x):

    return x + 2


print(plus_2(3))  # => 5

# Functions are first class
print(plus_2)  # => <function plus_2 at 0x101deb400>

# Functions are objects. That means we can feed them in as arguments!


def apply_twice(f, arg):
    return f(f(arg))


print(apply_twice(plus_2, 0))  # => 4


def might_not_return(x):
    if x % 2 == 0:
        return 'even'


print(might_not_return(2))  # => 'even'
print(might_not_return(3))  # => None

### Modules ###
math.pow(2, 3)  # => 8.0
m.pow(2, 3)
pow(2, 3)
pi

# More variable assignment examples: binding names to objects
a = 3
b = a
a += 4
a is b

a = [3, 4]
b = a
a.append(5)
a is b


def main():
    pass


if __name__ == '__main__':
    main()
