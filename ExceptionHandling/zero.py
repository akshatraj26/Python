

# c = a/b


try:
    a = int(input("Enter an Integer:-"))
    b = int(input("Enter an Integer:-"))
    c = a/b
    print("c=", c)
    
except ZeroDivisionError as ze:
    print("Denominator is 0")
    print(ze.args)
    print(ze)
    
except ValueError as e:
    print("Unable to convert string to int")
except:
    print("Some unknown error")
    