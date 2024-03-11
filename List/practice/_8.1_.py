lst  = ['Anil', 'Amol', 'Aditiya', 'Avi', 'Alka']
lst.insert(2, 'Anuj')
print(lst)
lst.append('Zulu')
print(lst)
lst.pop(4)
print(lst)
lst[0] = 'AnilKumar'
print(lst)

print(sorted(lst))
r = reversed(lst)
print(list(r))