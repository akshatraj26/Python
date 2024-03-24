def count_capital(string, count):
    if string == '':
        return count

    if string[0] >= 'A' and string[0] <= 'Z':
        count += 1

    count = count_capital(string[1:], count)
    print(string)
    return count

print(count_capital('Hi How are YOU. DOING', 0))