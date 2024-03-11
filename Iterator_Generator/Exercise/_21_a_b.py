"""
Write a program to flatten the following list:
"""
import time
mat1 = [[n for n in range(1,5)], [n for n in range(5,9)], [n for n in range(9, 13)]]
print(mat1)

lis = []
# start = time.perf_counter()
# for lis in mat1:
#     for ele in lis:
#         lis.append(ele)
# end = time.perf_counter()
# tim = end -start
print([num for arr in mat1 for num in arr])


