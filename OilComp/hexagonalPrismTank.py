class HexagonalPrismTank:
    def __init__(self, base_edge = 6, height = 400, lqd_height = 0):
        self.base_edge = base_edge
        self.height = height
        self.liquid_height = lqd_height
        self.max_volume = 2.5980762 * base_edge * base_edge * height
    
    def getCurrentVolume(self):
        return (2.5980762 * self.base_edge * self.base_edge 
            * self.liquid_height)
    
    def getMaxVolume(self):
        return self.max_volume
    
    def getAmntToFill(self):
        return self.max_volume - self.getCurrentVolume()
        
    def getAmntPartial(self, user_input):
        return user_input - self.liquid_height
    
    def setLiquidHeight(self, amnt_oil):
        self.liquid_height += amnt_oil