from projectile import projectile
from graph import graph

newGraph = graph()

def newObject():
    name = input("Enter the name of the new projectile: ")
    
    while True:
        try:
            xVelocity = float(input("Enter the horizontal velocity of the projectile: "))
            if xVelocity >= 0:
                break
            else:
                raise Exception
        except ValueError:
            print("The value you entered isn't a valid number.")
            pass
        except Exception:
            print("The value must be greater than or equal to zero")
    
    while True:
        try:
            yVelocity = float(input("Enter the vertical velocity of the projectile: "))
            if yVelocity >= 0:
                break
            else:
                raise Exception
        except ValueError:
            print("The value you entered isn't a valid number.")
            pass
        except Exception:
            print("The value must be greater than or equal to zero")
    
    while True:
        try:
            height = float(input("Enter the starting height of the projectile: "))
            if height >= 0:
                break
            else:
                raise Exception
        except ValueError:
            print("The value you entered isn't a valid number.")
            pass
        except Exception:
            print("The value must be greater than or equal to zero.")
    
    while True:
        try:
            gravity = float(input("Enter the gravitational field strength acting on the projectile: "))
            if gravity > 0:
                break
            else:
                raise Exception
        except ValueError:
            print("The value you entered isn't a valid number.")
            pass
        except Exception:
            print("The value must be greater than zero.")
    
    return projectile(name, xVelocity, yVelocity, height, gravity)

while True:
    try:
        noObjects = int(input("Enter the number of projectiles you would like to simulate: "))
        if noObjects > 0:
            break
        else:
            raise Exception
    except ValueError:
        print("The value you entered isn't a valid number")
    except Exception:
        print("The value must be greater than zero")

for _ in range(noObjects):
    print()
    newGraph.addLine(newObject())

newGraph.render()