# Projectile Simulator
Simulates the movement of an object based on: 
- Gravitational field strength
- Initial height of the object
- Initial velocity of the object

The model is limited to 2 dimensions and assumes no air resistance or any collisions, except for with the ground. Using matplotlib, a graph showing the height of the object as its horizontal distance varies is displayed.

The graph can handle multiple objects so that they can be compared on one graph.

# Usage
1. Run main.py
2. Enter how many projectiles should be simulated
3. For each projectile enter the values bearing in mind the follow requirements:
    - The name should be a string
    - The velocities and starting height should be a number greater than or equal to zero
    - The gravitational field strength should be a number greater than zero
4. After entering all of the values for the projectiles, the graph will automatically be displayed