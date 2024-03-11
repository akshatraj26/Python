def factorize(n, i):  # 455  2
    if i <= n:    # 2< = 455
        if n % i == 0:
            print(i, end=',')
            n = n // i

        else:
            i += 1
        factorize(n, i)


factorize(100, 2)

