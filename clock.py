class Clock:
    def __init__(self, hour, minute):
        total_minutes = (hour * 60) + minute
        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60
        self.hour = (self.hour + 24) % 24
        self.minute = (self.minute + 60) % 60

    def __repr__(self):
        return f"Clock({self.hour:02d}, {self.minute:02d})"
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
    
    def __eq__(self, other):
        other.hour = other.hour % 24
        other.minute = other.minute % 60
        if isinstance(other, Clock):
            return self.hour == other.hour and self.minute == other.minute
    
    def __add__(self, minutes):
        totalminutes = (self.hour * 60 + self.minute + minutes) % (24 * 60)
        return Clock(totalminutes // 60, totalminutes % 60)
        
    def __sub__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute - minutes) % (24 * 60)
        return Clock(total_minutes // 60, total_minutes % 60)
    

clock1 = Clock(8, 0)
clock2 = Clock(11, 9)
clock3 = Clock(24, 0)
clock4 = Clock(25, 0)
clock5 = Clock(100, 0)
clock6 = Clock(1, 60)
clock6 = Clock(0, 160)
clock7 = Clock(0, 1723)
clock8 = Clock(25, 160)
clock9 = Clock(201, 3001)
clock10 = Clock(72, 8640)
clock11 = Clock(-1, 15)
clock12 = Clock(-25, 0)
clock13 = Clock(-91, 0)
clock14 = Clock(1, -40)
clock15 = Clock(1, -160)
clock16 = Clock(1, -4820)
clock17 = Clock(2, -60)
clock18 = Clock(-25, -160)
clock19 = Clock(-121, -5810)
#Add minutes

clock20 = (Clock(10, 0) + 3)
clock21 = (Clock(6, 41) + 0)
clock22 = (Clock(0, 45) + 40)
clock23 = (Clock(10, 0) + 61)
clock24 = (Clock(0, 45) + 160)
clock25 = (Clock(23, 59) + 2)
clock26 = (Clock(5, 32) + 1500)
clock27 = (Clock(1, 1) + 3500)
#Subtract minutes
clock28 = (Clock(10, 3) - 3)
clock29 = (Clock(10, 3) - 30)
clock30 = (Clock(10, 3) - 70)
clock31 = (Clock(0, 3) - 4)
clock32 = (Clock(0, 0) - 160) 
clock33 = (Clock(6, 15) - 160)
clock34 = (Clock(5, 32) - 1500)
clock35 = (Clock(2, 20) - 3000)


print('Clock1:', clock1)  
print('Clock2:', clock2)  
print('Clock3:', clock3)  
print('Clock4:', clock4)  
print('Clock5:', clock5)  
print('Clock6:', clock6)  
print('Clock7:', clock7)  
print('Clock8:', clock8)  
print('Clock9:', clock9)  
print('Clock10:', clock10) 
print('Clock11:', clock11) 
print('Clock12:', clock12) 
print('Clock13:', clock13) 
print('Clock14:', clock14) 
print('Clock15:', clock15) 
print('Clock16:', clock16) 
print('Clock17:', clock17) 
print('Clock18:', clock18) 
print('Clock19:', clock19) 
print('Clock20:', clock20)
print('Clock21:', clock21)
print('Clock22:', clock22)
print('Clock23:', clock23)
print('Clock24:', clock24)
print('Clock25:', clock25)
print('Clock26:', clock26)
print('Clock27:', clock27)
print('Clock28:', clock28)
print('Clock29:', clock29)
print('Clock30:', clock30)
print('Clock31:', clock31)
print('Clock32:', clock32)
print('Clock33:', clock33)
print('Clock34:', clock34)
print('Clock35:', clock35)
