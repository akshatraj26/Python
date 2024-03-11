class Weather:
    def __init__(self):
        self.__params = ['temp', 'Rel Hum', 'Cloud Cover', 'Wind Vel']
        
    def __contains__(self, p):
        return p if p in self.__params else False
    
w = Weather()

if 'Rel Hum' in w:
    print("Valid Weather parameter")
    
    
else:
    print("Invalid weather parameter")