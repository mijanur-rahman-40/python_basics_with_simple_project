import one

print('Top level in two.py')
one.function()


if __name__ == "__main__":
    print("two.py is being run directly!")
else:
    print('Two.py has been imported!')


def f():
    return 4

ac = 'hello'

print
