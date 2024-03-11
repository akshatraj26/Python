import time

def timer(func):
    def calculate(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print()
        print(f"Finished {func.__name__!r} in {runtime:.8f} sec")
        return value
    return calculate

@timer
def product(num):
    fact = 1
    for i in range(num):
        fact = fact * i + 1
    return fact


@timer
def product_and_sum(num):
    p = 1
    for i in range(num):
        p = p * i + 1

    s = 0
    for i in range(num):
        s = s + i + 1

    return (p, s)


@timer
def time_pass(num):
    for i in range(num):
        i += 1


p = product(10)
print("Product of the first 10 number:- ", p)

p = product(20)
print("Product of the first 20 number:- ", p)

ps = product_and_sum(10)
print("Product and Sum of first 10 number:-", ps)

ps = product_and_sum(20)
print("Product and Sum of first 10 number:-", ps)


time_pass(20)
