"""
Write	a	program	to	calculate	sum	of	first	10	terms	of	the	following	series:
 1!	2!	+	2!	3!	+	3!	4!	+	4!	5!	+	……	+	9!	10
"""

for i in range(1, 11):
    prod1 = 1
    s = 0
    for j in range(1, i+1):
        print("j:-",j)
        prod1 *= j
        print("Prod1:-", prod1)
    prod2 = prod1 * (j+1)
    print("Prod2:-", prod2)
    term = prod1 * prod2
    s = s+term

print("Sum:-", s)