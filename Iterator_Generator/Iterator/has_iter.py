s = 'Hello'
lst = ['Focussed', 'bursts', 'of', 'activity']
print("Iterable")
print(hasattr(s, '__iter__'))
print(hasattr(s, '__next__'))
print()
print(hasattr(lst, '__iter__'))
print(hasattr(lst, '__next__'))

print("Iterator")
i = iter(s)
print(hasattr(i, '__iter__'))
print(hasattr(i, '__next__'))

print()
j = iter(lst)
print(hasattr(j, '__iter__'))
print(hasattr(j, '__next__'))