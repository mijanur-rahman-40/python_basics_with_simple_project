try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('General error! watch out!')


try:
    x = 5
    y = 0
    z = x / y
except:
    print('Error!')
finally:
    print('All done')
        