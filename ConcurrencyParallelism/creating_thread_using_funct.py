import threading


def print_cube(num):
    print(f"Cube: {num ** 3}")


def print_square(num):
    print(f"Square: {num ** 2}")


if __name__ == '__main__':
    t1 = threading.Thread(target=print_square, args=(12,))
    t2 = threading.Thread(target=print_cube, args=(10, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(vars(t1))
    print(vars(t2))

    print("Done!")
