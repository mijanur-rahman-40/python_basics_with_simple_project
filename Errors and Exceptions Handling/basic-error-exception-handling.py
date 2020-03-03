def addNumber(num1, num2):
    return num1 + num2


num1 = 10
num2 = input('Please give a number ')
# print(addNumber(num1, num2))

try:
    # want to attempt this code
    # may have an error
    result = 10 + '10'
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("add went well")
    print(result)

