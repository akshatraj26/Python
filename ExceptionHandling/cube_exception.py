"""
Write a program that receives 10 integers and stores them and their cubes in a dictionary.
If the number entered is less than 3, then raise a user-defined exception NumberTooSmall,
and if the number entered is more than 30,  then raise a user defined exception NumberTooBig. Whether an exception occurs
or not,  at the end print the contents of the dictionary.
"""


class NumberTooBig(Exception):
    def __init__(self, num):
        self.num = num

    def get_details(self):
        return f"Number too big, {self.num}"


class NumberTooSmall(Exception):
    def __init__(self, num):
        self.num = num

    def get_details(self):
        return f"Number too small, {self.num}"


class Cube:
    def __init__(self, lis):
        self.user_input = lis
        self.dict = {}

    def loop(self):
        for i in self.user_input:
            if i < 3:
                raise NumberTooSmall(i)
            elif i > 30:
                raise NumberTooBig(i)

            else:
                self.dict[i] = i ** 3

    def display(self):
        return self.dict


try:
    a = Cube([4, 5, 6, 7, 8, 9, 10,30, 2, 18])
    a.loop()
except NumberTooSmall as e:
    print(e.get_details())

except NumberTooBig as e:
    print(e.get_details())
finally:
    a.display()
