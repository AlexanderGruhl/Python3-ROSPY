from robot_control_class import RobotControl

class MoveRobot:
    def __init__(self, speed, f_time, t_time):
        self.rc = RobotControl()
        self.forward = "forward"
        self.clockwise = "clockwise"
        self.speed = speed
        self.f_time = f_time
        self.t_time = t_time
        self.rc.move_straight_time(self.forward, 1, 2)
    
    def square(self):
        for x in range(4):
            self.turn()
            self.move_forward()
        
    def move_forward(self):
        self.rc.move_straight_time(self.forward, self.speed, self.f_time)
    
    def turn(self):
        self.rc.turn(self.clockwise, self.speed, self.t_time)

s1 = MoveRobot(0.3, 4.0, 7.0)
s1.square()
s2 = MoveRobot(0.3, 8.0, 7.0)
s2.square()