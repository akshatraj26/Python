import json


def encode_complex(x):
    if isinstance(x, Complex):
        return {"__Complex__": True, 'real': x.real, 'imag': x.imag}
    else:
        raise TypeError('Complex object is not JSON serializable')


def decode_complex(dct):
    if "__Complex__" in dct:
        return Complex(dct['real'], dct['imag'])
    return dct


class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def print_data(self):
        print(self.real, self.imag)


c = Complex(1.0, 2.0)
with open('complex.json', 'w+') as f:
    json.dump(c, f, default=encode_complex)


with open('complex.json', 'r') as f:
    inc = json.load(f, object_hook=decode_complex)

inc.print_data()
