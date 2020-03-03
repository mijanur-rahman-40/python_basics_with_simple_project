def function():
    print('function() in one.py')


print('Top Level in one.py')

# when we run python file run like -> python one.py
# then it is true
if __name__ == "__main__":
    print('one.py is being run directly')
else:
    print('one.py has been imported!')
    

