class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age, end =' ')

        
class Student(Person):
    def __init__(self,name, age, roll_num, math, sci, hist):
        super().__init__(name, age)
        self.roll = roll_num
        self.math = math
        self.sci=sci
        self.hist = hist
    def display(self):
        super().display()
        print(self.roll, self.math, self.sci, self.hist)


lst = []
s = Student('Akshat', 23, 1234, 56, 78, 99)
lst.append(s)
s = Student('Ramesh', 34, 3445, 45, 46, 78)
lst.append(s)
s = Student('Rajesh', 73, 1334, 87, 98, 76)
lst.append(s)

for item in lst:
    item.display()



