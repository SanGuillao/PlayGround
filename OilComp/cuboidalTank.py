class CuboidalTank:
    def __init__(self, length = 10, width = 6, height = 400, lqd_height = 0):
        self.length = length
        self.width = width
        self.height = height
        self.liquid_height = lqd_height
        self.max_volume = length * width * height
    
    def getCurrentVolume(self):
        return self.liquid_height * self.length * self.width
    
    def getMaxVolume(self):
        return self.max_volume
    
    def getAmntToFill(self):
        return self.max_volume - self.getCurrentVolume()
        
    def getAmntPartial(self, user_input):
        return user_input - self.liquid_height
    
    def setLiquidHeight(self, amnt_oil):
        self.liquid_height += amnt_oil
    