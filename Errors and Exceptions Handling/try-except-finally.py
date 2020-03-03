try:
    f = open('testfile', 'r')
    f.write("write a test line")
except TypeError:
    print("there was an type error")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")


""" def askForInt():
    try:
        result = int(input("please provide a number: "))
    except:
        print("Whoops! That is not a number{}", result)
    finally:
        print("End of try/except/finally")


askForInt()
 """


def askForInt():
    while True:
        try:
            int(input("please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print('Yes thank yoy')
            break
        finally:
            print("End of try/except/finally")
            print('I will always run at the end')


askForInt()
