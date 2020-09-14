from robot_control_class import RobotControl
import time

class maze:
    def __init__(self):
        self.rc = RobotControl()
        self.speed = 0.3
        self.time = 4.5
        self.front_laser = 360
        self.end = False

    def move_maze(self):
        while self.end == False:
            self.move_decision()
                   
    def get_laser(self):
        l = self.rc.get_laser(self.front_laser)
        return l
    
    def get_laser_full(self):
        l = self.rc.get_laser_full()
        return l
    
    def move_straight(self):
        self.rc.move_straight()
    
    def stop_robot(self):
        self.rc.stop_robot()
    
    def move_straight_time(self):
        self.rc.move_straight_time("forward", self.speed, 20)
    
    def turn(self, direction):
        self.rc.turn(direction, self.speed, self.time)
    
    def forward_movement(self):
        l = self.get_laser()
        while l > 1:
            #print(l)
            self.move_straight()
            l = self.get_laser()
        self.stop_robot()
    
    def move_decision(self):
        if(max(self.get_laser_full()) > 100):
            print("in if")
            self.time = 5.2
            self.turn("counter-clockwise")
            self.move_straight_time()
            self.end = True
        elif(self.get_laser() > 1):
            self.forward_movement()
        elif(self.get_laser_full()[0] > 1):
            self.turn("clockwise")
        elif(self.get_laser_full()[719] > 1):
            self.turn("counter-clockwise")
        else:
            self.turn("clockwise")

r = maze()
r.move_maze()