import numpy as np
import matplotlib.pyplot as plt

class projectile:
    def __init__(self, name, xVelocity, yVelocity, height, gravity):
        self.name = name
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.height = height
        self.gravity = gravity
        self.calc()
    
    def calc(self):
        self.endTime = (self.yVelocity + (self.yVelocity ** 2 + 2 * self.gravity * self.height)**0.5) / self.gravity
        self.peakTime = self.yVelocity / self.gravity
        self.time = np.linspace(0, self.endTime, 100)
        self.xDistance = self.xVelocity * self.time
        self.yDistance = self.time * (self.yVelocity - (self.gravity * self.time) /  2) + self.height