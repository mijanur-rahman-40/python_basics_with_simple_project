basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# show that duplicates have been removed
print(basket)

# fast membership testing
print('orange' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print(a)

# letters in a but not in b
print(a - b)

# letters in a or b or both
print(a | b)

# letters in both a and b
print(a & b)

# letters in a or b but not both
print(a ^ b)

# Similarly to list comprehensions, set comprehensions are also supported
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

