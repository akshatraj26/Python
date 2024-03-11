class Product:
    def __init__(self):
        self.__title = input('Enter title: ')
        self.__price = input("Enter Price: ")
        
    def display_data(self):
        print(self.__title, self.__price)
        
class Sales:
    def __init__(self):
        self._sales_figures = [int(x) for x in input("Enter sales fig: ").split()]
        
    def display_data(self):
        print(self._sales_figures)
        
class HandWareItem(Product, Sales):
    def __init__(self):
        Product.__init__(self)
        Sales.__init__(self)
        self.__category = input("ENter Category:")
        self.__oem = input("Enter otem: ")
        
    def display_data(self):
         Product.display_data(self)
         Sales.display_data(self)
         print(self.__category, self.__oem)
         
hw1 = HandWareItem()
hw1.display_data()
hw2 = HandWareItem()
hw2.display_data()