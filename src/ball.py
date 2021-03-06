import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius
        self.num = 8

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball affected by gravity
    """
    GRAVITY = 0.1

    # TODO: 
    def update(self):
        self.velocity.y += self.GRAVITY
        super().update()
#     """
#     # TODO: 

# class RainbowBall(???):
#     """
#     Ball that changes colors
#     """
#     # TODO:
class Rainbow(Ball):

def update(self):
    r = (self.color[0] + 3) % 256
    g = (self.color[1] + 3) % 256
    b = (self.color[2] + 3) % 256

    self.color = [r, g, b]
    super().update()
#super is hertiting class


class BouncingRainbow(BouncingBall, RainbowBall):
    pass
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

# class KineticBall(???):
#      A ball that collides with other collidable balls using simple elastic circle collision
    
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        self.mass = mass
        super().__init__(bounds, position, velocity, color, radius)

    def collide(self, object, relative_vector):
        # print('bang!')
        
        # We can imagine the point of reflection as a wall tangent to the collision 
        tangent = math.atan2(relative_vector.y, relative_vector.x)
        # Get the angle of travel for both
        angle1 = 0.5 * math.pi - math.atan2(self.velocity.y, self.velocity.x)
        angle2 = 0.5 * math.pi - math.atan2(object.velocity.y, object.velocity.x)
        # The angles of travel are updated to be two times the tangent minus the current angle
        angle1 = 2 * tangent - angle1
        angle2 = 2 * tangent - angle2

        # Exchange speed
        # Get velocity of other particle
        object_speed = object.velocity.length()
        self_speed = self.velocity.length()

        # Update with new angle and opposing particle's speed
        self.velocity = Vector2(math.sin(angle1), math.cos(angle1)) * object_speed
        object.velocity = Vector2(math.sin(angle2), math.cos(angle2)) * self_speed

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
