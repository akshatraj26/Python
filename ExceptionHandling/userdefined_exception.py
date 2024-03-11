class InsufficientBalanceError(Exception):
    def __init__(self, accno, cb):
        self.__accno = accno
        self.__cb = cb
        
    def get_details(self):
        return {'Acc no' : self.__accno,
                'Current Balance': self.__cb}
        
class Customers:
    def __init__(self):
        self.__dct = {}
        
    def append(self, accno, n, bal):
        self.__dct[accno] = {'Name':n, 'Balance': bal}
        
    def deposit(self, accno, amt):
        d = self.__dct[accno]
        d['Balance'] += amt
        self.__dct[accno] = d
        
    def display(self):
        for k, v in self.__dct.items():
            print(k, v)
        print()
        
    def withdraw(self, accno, amt):
        d = self.__dct[accno]
        curbal = d['Balance']
        if curbal - amt < 5000:
            raise InsufficientBalanceError(accno, curbal)
        
        else:
            d['Balance'] -= amt
            self.__dct[accno] = d
        
c = Customers()
c.append(123, 'Sanjay', 5000)
c.append(101, 'Akshat', 5000)
c.append(120, 'Amogsidh', 50000)
c.append(150, "Saket", 3454545)
c.display()
c.deposit(123, 10000)
c.deposit(120, 75754732547)
c.display()

try:
    c.withdraw(101, 500)
    print("Amount withdrawn successfully")
    c.display()
    c.withdraw(123, 100)
    print("Amount Withdrawn successfully")
    c.display()
except InsufficientBalanceError as ibe:
    print("Withdrawal denied")
    print("Insufficient balance")
    print(ibe.get_details())