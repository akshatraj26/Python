li = list()
tu = tuple()
se = set()
di = dict()


# s = {[10, 20, 30], [10, 20, 30]}
# print(s)

lis = [10, 20, 30, 40, 10, 30]
# [40, 10, 20, 30]

print(lis[3:5] + lis[1:3])
print(set(lis))

print(f"{round(2334.4, 3):^10}")

#
# def print_centered_float(number):
#   """Prints a float centrally justified in 10 columns, with 3 places beyond the decimal point.
#
#   Args:
#     number: The float to be printed.
#   """
#
#   formatted_number = f"{number:.3f}"  # Format the number with 3 decimal places
#   spaces_before = (10 - len(formatted_number)) // 2  # Calculate number of spaces before
#   spaces_after = 10 - len(formatted_number) - spaces_before  # Calculate number of spaces after
#   print(" " * spaces_before + formatted_number + " " * spaces_after)
#
# # Example usage
# number = 3.14159
# print_centered_float(number)

#
# l, b, h = input('Enter length, breadth & height:')
# print(l, b, h)

lst = []
# lst.add(45)
print(lst)


tpl = ((1, 5), (2, 3), (4, 5))
for x, y in tpl:
    print(x, y)

s = {27, 42, 12}
# s.del(42)
print(s)