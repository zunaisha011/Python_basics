try:
    result = 10 / 0 
    print(result)
except ZeroDivisionError:
    print('Error')

# ZeroDivisionError occurs when you try to divide by zero.
# NameError it means that you tried to use the variable a when it was not defined.
# IndexError it occured because you tried to access data from a list using an index that does not exist for this list.


a=5
try:
    b=int(input('Enter number'))
    c=a/b
    print(c)
except:
    print('wrong int')



a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")


a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("Success a=",a)
        

a = 8
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("Success a=",a)
finally:
    print("Processing Complete")


