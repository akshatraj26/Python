"""
Write a recursive function to obtain average of all numbers present in a given list.
"""




def average(lst, len_lis):
    if len_lis == 0:
        return 0

    else:
        return (average(lst, len_lis -1) * (len_lis -1) + lst[len_lis - 1]) / len_lis


num_lis = [12, 11, 13, 14, 15, 16]
avg = average(num_lis, len(num_lis))
print(avg)

