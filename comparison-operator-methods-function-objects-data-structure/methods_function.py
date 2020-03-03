my_list = [1, 2, 3]
print(help(my_list.insert))

print('\n####--------------------------####-------------------------####\n')


# define function
def name_function():
    '''
    DOCSTRING : Information about the function
    :return:
    '''
    print("hello")


help(name_function())


def say_hello(name='NAME'):
    print('hello ' + name)


say_hello()

print('\n####--------------------------####-------------------------####\n')


def dog_check(my_string):
    return 'dog' in my_string.lower()


print(dog_check('Dog ran away'))

print('\n####--------------------------####-------------------------####\n')


def pig_latin(word):
    first_letter = word[0]

    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('word'))
print('\n####--------------------------####-------------------------####\n')


def my_function(a, b, c=0, d=0, e=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05


print(my_function(40, 60, 100, 100))

print('\n####--------------------------####-------------------------####\n')


# using args as function parameter
# def arg_function(*args):
#     print(args)
def arg_function(*spam):
    for item in spam:
        print(item)
    print(spam)


arg_function(40, 60, 100, 1, 34)

print('\n####--------------------------####-------------------------####\n')


# key words argument
def my_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print('I did not find any fruit here')


my_func(fruit='apple', veggle='lettuce')

print('\n####--------------------------####-------------------------####\n')


# both arguments
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")


func(10, 20, 30, fruit='orange', food='eggs', animal='dog')
print('\n####--------------------------####-------------------------####\n')


def animal_crackers(text):
    word_list = text.upper().split()
    print(word_list)


animal_crackers('Levelheaded apple')

print('\n####--------------------------####-------------------------####\n')


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald('macdonald'))

print('\n####--------------------------####-------------------------####\n')

myList = ['a', 'b', 'c']
print('--'.join(myList))


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

print('\n####--------------------------####-------------------------####\n')


# reverse word list
def master_yoda(text):
    word_list = text.split()
    reverse_word_list = word_list[::-1]
    return ' '.join(reverse_word_list)


word = master_yoda('I am in home')
print(word)

print('\n####--------------------------####-------------------------####\n')

# given a list of int s,return true if the array contains a 3 next to a 3
# somewhere

number = [1, 2, 3, 4, 5, 6]
for i in range(0, 4):
    print(number[i])


def has_33(number):
    for j in range(0, len(number) - 1):
        # if number[j] == 3 and number[j + 1] == 3:
        # or
        if number[j:j + 2] == [3, 3]:
            return True

    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))

print('\n####--------------------------####-------------------------####\n')


# character result
def paper_doll(text):
    result = ' '
    for char in text:
        result += char * 3
    return result


print(paper_doll('Hello'))

print('\n####--------------------------####-------------------------####\n')


# sum keyword
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

print('\n####--------------------------####-------------------------####\n')


# summer of
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 3, 5]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([4, 5, 6, 7, 8, 9]))


# spy game
def spy_game(nums):
    code = [0, 0, 7, 'x']
    # [0, 7, 'x']
    # [ 7, 'x']
    # ['x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# pop function
numArray = [55, 24, 63, 44, 15, 69]
temp = numArray.pop(2)
print(temp)
