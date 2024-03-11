nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']



res = list(map(lambda x, y: (x, y), nums, strs))
print(res)