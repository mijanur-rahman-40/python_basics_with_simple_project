tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guide'] = 4127
print(tel)
print(tel['jack'])
# del tel['sape']

print(list(tel))
print(sorted(tel))

print('guide' in tel)
print('jack' not in tel)


# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dictionary)

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
print({x: x ** 2 for x in (2, 4, 6)})


    
