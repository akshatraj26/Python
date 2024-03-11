def fun(num):
    if num == 0:
        print("False")
    if num == 1:
        print("True")
    if num % 2 == 0:
        fun(num / 2)

fun(256)

print()