import numpy as np
import matplotlib.pyplot as plt

gravity = 9.81

class projectile:
    def __init__(self, name, yVelocity, xVelocity, height):
        self.name = name
        self.yVelocity = yVelocity
        self.xVelocity = xVelocity
        self.height = height
        self.calc()
    
    def calc(self):
        self.endTime = (self.yVelocity + (self.yVelocity ** 2 + 2 * gravity * self.height)**0.5) / gravity
        self.peakTime = self.yVelocity / gravity
        self.time = np.linspace(0, self.endTime, 100)
        self.xDistance = self.xVelocity * self.time
        self.yDistance = self.time * (self.yVelocity - (gravity * self.time) /  2) + self.height