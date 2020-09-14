from robot_control_class import RobotControl

rc = RobotControl()

def run_robot():
    s = rc.move_straight_time("forward", 2, 5)
    print("Straight motion: ", s)
    t = rc.turn("clockwise", 3, 7)
    print("Clockwise motion: ", t)

run_robot()