from robot_control_class import RobotControl

rc = RobotControl()

def run_robot():
    t = rc.turn("counter-clockwise", 1, 2.85)
    print("Clockwise motion: ", t)
    s = rc.move_straight_time("forward", 1, 1)
    print("Straight motion: ", s)
    t = rc.turn("counter-clockwise", 1, 1.7)
    print("Clockwise motion: ", t)
    s = rc.move_straight_time("forward", 1, 1)
    print("Straight motion: ", s)
    

run_robot()