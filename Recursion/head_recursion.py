def headprint(n):

    if n == 0:
        return
    else:

        # print( n, end=' ')

        headprint(n-1)
        print(n, end=' ')


# 10
# 9
# 8
#


headprint(10)
#
# def tailprint(n):
#     if n == 22:
#         return
#     else:
#         print(n)
#         tailprint(n+1)
# print()
# tailprint(10)