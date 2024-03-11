def helper(n, t, lol):
    global j
    if len(t) == n:
        lol[j] = lol[j] + t
        j += 1
        return

    for k in range(1, n+1):
        t.append(k)
        helper(n, t, lol)
        t.pop()

def generate(n):
    t = []
    lol = [[] for i in range(n ** n)]
    helper(n, t, lol)
    return lol

j = 0
i = generate(3)
print(i)