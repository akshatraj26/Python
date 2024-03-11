def generate(n):
    lol = [[] for i in range(n*n)]
    pos =0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                t = [i, j, k]
                lol[pos] = t
            pos += 1

    return lol

f = generate(3)
print(f)