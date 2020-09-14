from robot_control_class import RobotControl
import time

rc = RobotControl()

def move_x_seconds(move):
    rc.move_straight()
    time.sleep(move)
    rc.stop_robot()

a = int(input("Move for how long? "))
move_x_seconds(a)