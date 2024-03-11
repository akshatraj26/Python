"""
Queue data structures First In First Out
"""
from collections import deque
q = deque()

q.append('Suhana')
q.append('Akshat')
q.append("HariOm")
q.append("RIshi")
q.append("AmogSidh")
print(q)
print()
print(type(q))


print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)