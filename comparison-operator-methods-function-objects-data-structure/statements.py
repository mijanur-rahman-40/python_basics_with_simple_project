# ---------------- if else elif --------------- #
print('if else elif\n')
if True:
    print('this is true')

hungry = False
if hungry:
    print('FEED ME')
else:
    print('DO NOT FEED ME')

location = 'Bank'
if location == 'Auto shop':
    print('Cars are coll!')
elif location == 'Bank':
    print('Money is cool!')
else:
    print('I do not know  much')

print('\n####--------------------------####-------------------------####\n')

# ---------------- for loop --------------- #
print('for loop\n')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    print(num)

print('\n####--------------------------####-------------------------####\n')

print('\n')
for val in my_list:
    # Check for even
    if val % 2 == 0:
        print(val)
    else:
        print(f'{val} is Odd number')
list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(f'The sum of all number is : {list_sum}')

print('\n####--------------------------####-------------------------####\n')

print('\n')
# print string
my_sting = 'Hello world'
for letter in my_sting:
    print(letter)

print('\n####--------------------------####-------------------------####\n')

print('\n')
tup = (1, 2, 3)
for item in tup:
    print(item)

print('\n####--------------------------####-------------------------####\n')
print('\n')
m_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
length = len(m_list)
print(f'len is {length}')
for item in m_list:
    print(item)

print('\n####--------------------------####-------------------------####\n')
print('\n')
for (a, b) in m_list:
    print(a)
    print(b)

print('\n####--------------------------####-------------------------####\n')
print('\n')
num_list = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in num_list:
    print(b)

print('\n####--------------------------####-------------------------####\n')
print('\n')
dictionary = {'k1': 1, 'k2': 2, 'k3': 3}
for item in dictionary:
    print(item)
for item in dictionary.items():
    print(item)
for value in dictionary.values():
    print(value)
for key, value in dictionary:
    print(value)

print('\n####--------------------------####-------------------------####\n')
# ---------------- while loop --------------- #
print('while loop\n')
x = 0
while x < 5:
    print(f'The current value x is {x}')
    x = x + 1
else:
    print('X is not less than 5')
y = [1, 2, 3]

for item in y:
    # comment
    pass
print('end of script')

print('\n####--------------------------####-------------------------####\n')
print('\n')
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue
    print(letter)

print('\n####--------------------------####-------------------------####\n')
print('\n')
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        break
    print(letter)

print('\n####--------------------------####-------------------------####\n')
print('\n')
z = 0
while z < 5:
    if z == 2:
        break
    # print(z)
    z = z + 1

print('\n####--------------------------range-------------------------####\n')
# ---------------- range --------------- #
print('\nrange\n')
my_list = [1, 2, 3]
for num in range(11):
    print(num)
for num in range(2, 11):
    print(num)
for num in range(1, 11, 4):
    print(num)
print(list(range(0, 11, 3)))
index_count = 0
for letter in 'apple':
    # print('At index {} the letter is {}'.format(index_count, letter))
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1
word = 'umbrella'
for item in enumerate(word):
    print(item)
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
print('\n####--------------------------####-------------------------####\n')
# ---------------- zip --------------- #
# The zip() function returns a zip object, which is an iterator
# of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
print('\nzip\n')
list_1 = [1, 2, 3]
list_2 = ['q', 'b', 'c']
print(zip(list_1, list_2))
for item in zip(list_1, list_2):
    print(item)
list_1 = [1, 2, 3, 4, 5, 6, ]
list_2 = ['q', 'b', 'c']
list_3 = [100, 200, 300]
print(zip(list_1, list_2))
for item in zip(list_1, list_2, list_3):
    print(item)
for x, y, z in zip(list_1, list_2, list_3):
    print(x)
    print(z)
    print('\n')
print(list(zip(list_1, list_2, list_3)))

print('\n####--------------------------####-------------------------####\n')
# --------------- finding equality ---------------------- #
print('x' in ['y', 'x', 'z'])
print('a' in 'a world')
print('myKey' in {'myKey': 345})

d = {'myKey': 345}
print(345 in d.values())
print(345 in d.keys())

my_list = [10, 100, 200]
print(max(my_list))
print(min(my_list))

# from random import
from random import shuffle

# here shuffle is in-place function ,so this returns nothing
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
shuffle(my_list)
print(my_list)

print('\n####--------------------------####-------------------------####\n')
# --------------- random ---------------------- #
print('\nrandom')
from random import randint

print(randint(0, 99))

print('\n####--------------------------####-------------------------####\n')
# --------------- input ----------------------- #
print('\ninput')
result = input('What is your name : ')
print(type(result))
print(result)

number = (input('What is your name : '))
print(type(number))
print(number)

# Statement Assessment 
str = 'Print only the words that start with a in this sentence'

for word in str.split():
    if (word[0].lower() == 's'):
        print(word)
    

