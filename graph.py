import matplotlib.pyplot as plt

class graph:
    def __init__(self):
        pass
    
    def addLine(self, obj):
        plt.plot(obj.xDistance, obj.yDistance, label = obj.name)
    
    def render(self):
        plt.legend()
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.show()