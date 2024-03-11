# When Base class is inherited by multiple subclasses then it is called as a Heirarchical inheritance.
class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the bird can fly but some cannot")
        
class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")
    
class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")
        
        
bird_obj = Bird()
sparrow_obj =Sparrow()
ost_obj = Ostrich()

for bird in (bird_obj, sparrow_obj, ost_obj):
    bird.intro()
    bird.flight()
    
print("\n")
#####################################################################################
class India:
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the widely spoken in India")
    def type(self):
        print("India is a developing country.")
        
class USA:
    def capital(self):
        print("Washington, D.C is the Capital of USA.")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developing country.")
        
        
ind = India()
usa = USA()

for country in (ind, usa):
    country.capital()
    country.language()
    country.type()