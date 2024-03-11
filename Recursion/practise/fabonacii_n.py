def fibbo(old, current, terms):
    if terms >= 1:
        new = old + current
        print(f"{new}", end="\t")
        terms -= 1
        fibbo(current, new, terms)

old = 1
current =1
print(f"{old}", end='\t')
print(f"{current}", end='\t')
fibbo(1, 1, 20)