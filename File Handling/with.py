with open('messages', 'r') as f:
    data = f.read(1)
    d = f.read(3)
    print(data, d)