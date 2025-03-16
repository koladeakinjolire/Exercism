import random
import string
import re
class Robot:
    existing_names = []
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.name = self.generate_name() 
        
    def generate_name(self):
        retry_limit = 100
        for _ in range(retry_limit):
            new_name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))
            if new_name not in Robot.existing_names:
                Robot.existing_names.append(new_name)
                self.name = new_name
                return self.name
                
        raise ValueError('No unique name available')
                
              
                
        
    def reset(self):
       try:
            Robot.existing_names.remove(self.name)
            self.name = '' 
            self.name = self.generate_name()
       except ValueError:
            print(f"Error: Name '{self.name}' not found in existing names. Reset failed.")
            

            
        

if __name__ == "__main__":
    robot_names = []
    pattern = r"[A-Z]{2}[0-9]{3}"
    robots = [Robot() for _ in range(1,11)]
    robot_names = [robot.name for robot in robots]
    print('Robot names are unique:', len(robot_names) == len(set(robot_names)))
    print('Existing names list matches current names', set(robot_names) == set(Robot.existing_names))
    robot1 = robots[0]
    robot2 = robots[1]
    r1_first_name = robot1.name
    r2_name = robot2.name
    print('Robot1 name: ', r1_first_name)
    print('Robot2 name: ', r2_name)
    assert re.match(pattern , r1_first_name) , 'Robot1 name is in an invalid format'
    assert re.match(pattern , r2_name), 'Robot2 name is in an invalid format'
    print('Robot1 name is the same as Robot2 name', r1_first_name == r2_name)
    robot1.reset()
    r1_new_name = robot1.name
    if r1_first_name != r1_new_name and r1_first_name not in Robot.existing_names:
        print("Robot1 name has been reset successfully.")
    else:
        print("Robot1 name reset failed.")
    print('Old name still exists after reset:', r1_first_name in Robot.existing_names)
    print('Robot1 new name after reset: ', r1_new_name)
    assert r1_new_name not in robot_names[:-1]
    robot1.reset()
    r1_newer_name = robot1.name
    print('Old name (r1_first_name) no longer exists:', r1_first_name not in Robot.existing_names)
    print('New name (r1_new_name) no longer exists:', r1_new_name not in Robot.existing_names)
    print('Newest name (r1_newer_name) exists:', r1_newer_name in Robot.existing_names)
    assert r1_first_name not in Robot.existing_names
    assert r1_new_name not in Robot.existing_names
    assert r1_newer_name in Robot.existing_names
    
   
