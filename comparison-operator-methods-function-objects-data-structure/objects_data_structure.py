# number
print('hello world')
print(2 ** 3)
print(3 / 2)
print(20 % 2)
print(2 + 10 * 10 + 3)
print((2 + 10) * (10 + 3))

print('\n####--------------------------####-------------------------####\n')
# --------------value assign----------- #
a = 5
print(a)
a = 10
print(a)
print(a + a)
print(a)
a = a + a
print(a)

print('\n####--------------------------####-------------------------####\n')
# --------------find type--------------  #
print(type(a))
a = 23.1
print(type(a))
print('\n####--------------------------####-------------------------####\n')
# --------------string-----------------  #
print('hello')
print("world")
print('this is also a string')
print("I'm going to run")
print('\n####--------------------------####-------------------------####\n')
# new line print
print('hello \nworld')
print('hello \n world')

print('\n####--------------------------####-------------------------####\n')
# tab
print('hello \tworld')
print(len('hello'))
print(len('I am'))

print('\n####--------------------------####-------------------------####\n')
# indexing
myString = 'Hello World'
print(myString[0])
print(myString[5])
print(myString[7])
print(myString[-1])
print(myString[-8])

print('\n####--------------------------####-------------------------####\n')
# print after 2 index with 2
print(myString[2:])
print(myString[:3])
print(myString[2:5])

print('\n####--------------------------####-------------------------####\n')
# print after two length string
# step size
name = 'i am apple'
print('step size')
print(name[::2])
print(name[::-1])
apple = name.split()
print(apple[::-1])

print('\n####--------------------------####-------------------------####\n')
# starting index 2
# ending index 7
# substring len 2
print(myString[2:7:2])
print(myString[::-1])

print('\n####--------------------------####-------------------------####\n')
# Immutability of string
# if a string is name = "San" then name[0] = 'p' is not valid
# concatenation is the solution
name = 'Sam'
last_letters = name[1:]
print(last_letters)
value = 'P' + last_letters
print(value)
let = name + " it is beautiful outside!"
print(let)
letter = 'Z'
letter = letter * 10
print(letter)
print('2' + '3')

print('\n####--------------------------####-------------------------####\n')
# upper to lower
x = 'Hello World'
print(x.upper())
print(x.upper)
print(x.lower())

print('\n####--------------------------####-------------------------####\n')
# split string
y = 'Hi this is a string'
print(y)
print(y.split())
print(y.split('i'))
x = 'Sam print only the words that start with s in this sentence'
for word in x.split():
    if word[0] == 's':
        print(word)

print('\n')

print('\n####--------------------------####-------------------------####\n')

# string formatting with the .format() method
# String here {} then also {}'.format('something1','something1')
print('This is a string {}'.format('INSERTED'))
print('This is a string {} {}'.format('INSERTED', 'DELETED'))
print('The {2} {0} {1}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

print('\n####--------------------------####-------------------------####\n')
# Float formatting follows "{value:width.precision f}"
result = 100 / 777
print(result)
# here width basically a white space
print('The result was {r:7.3f}'.format(r=result))
num = 104.123456
print('The result was {r:17.3f}'.format(r=num))

print('\n####--------------------------####-------------------------####\n')
# F string or formatted string literals
name = "Jose"
print(f'Hello, his name is {name}')
name = 'Sam'
age = 3
print(f'{name} is {age} years old.')

print('\n####--------------------------####-------------------------####\n')
# ----------------list------------------- #
my_list = [1, 2, 3, 4]
print(my_list)
my_list = ['STRING', 100, 23, 2.4]
print(my_list)
print(len(my_list))
num_list = ['one', 'two', 'three']
print(num_list[0])
print(num_list[1:])
another_list = ['four', 'five', 'six']
print(num_list + another_list)
num_list[0] = 'ONE ALL CAPS'
print(num_list)
print(num_list.append('seven'))
print(num_list)
print(num_list.pop())
print(num_list)
print(num_list.pop(0))
print(num_list.pop(-1))

print('\n####--------------------------####-------------------------####\n')
# sort function
char_arr = ['a', 'x', 'f', 'a']
num_arr = [1, 4, 1, 4, 6]
char_arr.sort()
print(char_arr)
num_arr.sort()
print(num_arr)
print(num_arr.sort())
my_list = [10, 20, 30, 100]
print(max(my_list))

print('\n####--------------------------####-------------------------####\n')
# ----------------- Dictionaries --------------- #
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.88}
print(prices_lookup['apple'])

print('\n####--------------------------####-------------------------####\n')
# dict in dict
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insideKey'])
print(d['k2'][2])

print('\n####--------------------------####-------------------------####\n')
# swap value id dict
d = {'key1': ['a', 'b', 'c']}
my_list = d['key1']
print(my_list)
letter = my_list[2]
print(letter.upper())
print(d['key1'][2].upper())
print('\n####--------------------------####-------------------------####\n')
# replace key value
d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)
print(d.keys())
print(d.values())
print(d.items())

print('\n####--------------------------####-------------------------####\n')
# ------------------- Tuple --------------------- #
t = (1, 2, 3)
print(type(t))
print(len(t))
print(t)
t = ('one', 2)
print(t[0])
print(t[-1])
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
# t[0] = 'NEW'

print('\n####--------------------------####-------------------------####\n')
# ------------------- Sets ----------------------- #
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_list = [1, 1, 11, 1, 2, 2, 23, 3, 33, 3, 3, 4, 4, 4]
print(set(my_list))

print('\n####--------------------------####-------------------------####\n')
# ------------------- Booleans -------------------- #
print(type(False))
print(1 > 2)
print(1 == 1)

print('\n####--------------------------####-------------------------####\n')
# ------------------ File ---------------------- #
# create_file = open("file_name.txt", "w+")
# create_file.write("hello \n ting tong ")
file_open = open('file_name.txt', 'r')

print('\n####--------------------------####-------------------------####\n')

# print(file_open.read())
print(file_open.readline())
print(file_open.readline(), end="#")
print(file_open.readline())
print(file_open.readline(5))

file_open = open('file_name.txt', 'w')

f1 = open('abc', 'w')
f1.write('something')
f1.write('\nvery special')

print('\n####--------------------------####-------------------------####\n')
# update file data
f1 = open('abc', 'a')
f1.write('\ngood')

# read data

# f1 = open('abc', 'r')
# for data in f1:
#     print(data)
#
# for value in f1:
#     file_open.write(value)
#
# read_image = open('img.jpg', 'rb')
# for i in read_image:
#     print(i)
# write_image = open('image.JPG', 'wb')
# for j in read_image:
#     write_image.write(j)
