import json


# Serialization and deserialization of employee
def encode_employee(x):
    if isinstance(x, Employee):
        return (x.ecode, x.ename, x.doj, x.sal)
    else:
        raise TypeError("Complex object is serializable to JSON")


def decode_employee(dct):
    if 'Employee' in dct:
        return Employee(dct['ecode'], dct['ename'], dct['doj'], dct['sal'])
    return dct


class Employee:
    def __init__(self, ecode, ename, doj, sal):
        self.ecode = ecode
        self.ename = ename
        self.doj = doj
        self.sal = sal

    def print_data(self):
        print(self.ecode, self.ename, self.doj, self.sal)


e = Employee('101', 'Amogsidh', '12/03/2024', 50000)
f = open('c_f', 'w+')
json.dump(e, f, default=encode_employee)
f.seek(0)
ine = json.load(f, object_hook=decode_employee)
print(ine)
