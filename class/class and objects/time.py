class Time:
    def __init__(self, hours = 0, minutes =0, seconds =0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"
    
    @staticmethod
    def from_seconds(seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return Time(hours, minutes, seconds)
    
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __add__(self, other):
        secs = self.total_seconds() + other.total_seconds()
        return Time.from_seconds(secs)
    
    def __sub__(self,other):
        sec = self.total_seconds() - other.total_seconds()
        return (Time.from_seconds(sec))

    
time = Time(4, 50, 45)
t2 = Time(12, 50, 45)
print(time)
print(t2)
print(t2.total_seconds())

print(time + t2)
print(time -t2)