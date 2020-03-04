# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method

import math
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)
    

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for question, answer in zip(questions, answers):
    # print('What is your {}? It is {}'.format(question, answer))
    print('What is your {0}? It is {1}'.format(question, answer))


# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

for i in reversed(range(1, 10, 2)):
    print(i)


# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):
    print(fruit)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
