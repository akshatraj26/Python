def papersizes(i, n, l, b):
    if n != 0:
        print(f"A{i}: L = {int(l)} B = {int(b)}")
        new_b = l / 2
        new_l = b
        n -= 1
        i += 1
        papersizes(i, n, new_l, new_b)


papersizes(0, 7, 1189, 841)