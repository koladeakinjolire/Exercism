# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 0
WEST = 3
SOUTH = 1


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def move(self, instruction):
        for cmd in instruction:
            if cmd == 'A':
                if self.direction == NORTH:
                    self.y_pos += 1
                elif self.direction == SOUTH:
                    self.y_pos -= 1
                elif self.direction == EAST:
                    self.x_pos += 1
                elif self.direction == WEST:
                    self.x_pos -= 1
            elif cmd == 'R':
                self.direction = (self.direction  + 1) % 4
            elif cmd == 'L':
                self.direction = (self.direction - 1) % 4
                
        return self.coordinates 
    
robot = Robot(EAST, 2, -7)
print(robot.move("RRAAAAALA"))
robot2 = Robot(NORTH, 5, 6)
print(robot2.move("RARLAARALARALAARAL"))
robot3 = Robot(EAST, 1, -6)
print(robot3.move("RARARALLARRARARA"))
robot4 = Robot(SOUTH, 0, 0)
print(robot4.move("RARARARLARARALALARARA"))
robot5 = Robot(WEST, 0, 0)
print(robot5.move("R"))
robot6 = Robot(NORTH, 0, 0)
print(robot6.move("L"))
robot7 = Robot(SOUTH, 8, 4)
print(robot7.move("LAAARRRALLLL"))
robot8 = Robot(EAST, 2, -7)
print(robot8.move("RRAAAAALA"))
robot9 = Robot(NORTH, 0, 0)
print(robot9.move("LAAARALAARALALRALRLALRALR"))
robot10 = Robot(NORTH, 0, 0)
print(robot10.move("L"))