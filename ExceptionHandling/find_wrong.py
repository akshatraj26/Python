# try:
#     45 /0
#
#
# except:
#     print("Unknown error")
# except ZeroDivisionError:
#     print("Cannot divide by 0")

def fun():
    try:
        return 30

    finally:
        return 34

k = fun()
print(k)