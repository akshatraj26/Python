def create_array(i, j, k, num):
    l = [[[num for col in range(k)] for row in range(j)] for rowcol in range(i)]
    return l

d = create_array(3, 5, 6, 40)
print(d)

    