"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0 #class

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self): #use self and/or attributes when creating methods inside classes
        self.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True

        return False


    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    # Placeholder for collision detection
    def collision_detection(self, other):
        pass  # Implement logic to determine collision

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
 
def new_aliens_collection(position_list):
    alien_list = []
    for position in position_list:
        new_alien = Alien(*position) #unpacks position tuple and makes it an attribute of new alien 
        alien_list.append(new_alien)
    return alien_list