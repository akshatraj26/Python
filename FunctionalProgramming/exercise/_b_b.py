lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]
import math
def area(n):
    return math.pi *  n * n

ar = list(map(area, lst))
print(ar)