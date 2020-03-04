from math import pi
from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.index('banana'))
# Find next banana starting a position 4
print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape')
fruits.sort()
fruits.pop()
print(fruits)


# using lists as stacks
stack = [3, 5, 4]
stack.append(8)
stack.pop()
print(stack)

# using lists as a Queues
queue = deque(["Eric", "John", "Michael"])
queue.append('Bob')
print(queue)
print(queue.popleft())
print(queue)


# list comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)
# same thing is done by
# We can calculate the list of squares without any side effects using

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

# or equivalently
squares = [x ** 2 for x in range(10)]
print(squares)

# list included with for and if clauses
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# if included in list
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])


# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# call am method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([number for element in vec for number in element])

# List comprehensions can contain complex expressions and nested functions:
print([str(round(pi, i)) for i in range(1, 6)])

# Nested list comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# the same output we can get in easy form
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# the most easiest way
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcamp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


print(transposed)

# we can get the same output by implementing a build in function
print(list(zip((*matrix))))

