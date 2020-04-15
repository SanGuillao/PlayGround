import math
class CylindricalTank:
    def __init__(self, radius = 6, height = 400, lqd_height = 0):
        self.radius = radius
        self.height = height
        self.liquid_height = lqd_height
        self.max_volume = math.pi * radius * radius * height
        
    def getCurrentVolume(self):
        return self.liquid_height * math.pi * self.radius * self.radius
    
    def getMaxVolume(self):
        return self.max_volume
    
    def getAmntToFill(self):
        return self.max_volume - self.getCurrentVolume()
        
    def getAmntPartial(self, user_input):
        return user_input - self.liquid_height
    
    def setLiquidHeight(self, amnt_oil):
        self.liquid_height += amnt_oil