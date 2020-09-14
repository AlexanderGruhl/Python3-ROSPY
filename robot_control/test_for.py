from robot_control_class import RobotControl

largest = 0
rc = RobotControl()
laser = rc.get_laser_full()

for c in laser:
    if largest < c:
        largest = c

print("The highest value in the list is: ", largest)