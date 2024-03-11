def frequency(s):
    freq = {}
    for word in s.split():
        # print(word)
        freq[word] = freq.get(word, 0) +1

    return freq

f = "It is true for all that that that that that  that all  refers to is not the same that that refers to "

d = frequency(f)
words = sorted(d)


for w in words:
    print("%s:%d" % (w, d[w]))