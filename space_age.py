class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def __str__(self):
        return str(self)
    
    def on_mercury(self):
        year = 31557600 * 0.24
        age = self.seconds / year
        return round(age, 2)
    
    def on_venus(self):
        year = 31557600 * 0.62
        age = self.seconds / year
        return round(age, 2)
    
    def on_earth(self):
        year = 31557600
        age = self.seconds / year
        return round(age, 2)
    
    def on_mars(self):
        year = 31557600 * 1.88
        age = self.seconds / year
        return round(age, 2)
    
    def on_jupiter(self):
        year = 31557600 * 11.86
        age = self.seconds / year
        return round(age, 2)
    
    def on_saturn(self):
        year = 31557600 * 29.45
        age = self.seconds / year
        return round(age, 2)
    
    def on_uranus(self):
        year = 31557600 * 84.02
        age = self.seconds / year
        return round(age, 2)
    
    def on_neptune(self):
        year = 31557600 * 164.79
        age = self.seconds / year
        return round(age, 2)
    
print(SpaceAge(1000000000).on_earth())
print(SpaceAge(1000000000).on_mercury())