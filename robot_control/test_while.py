from robot_control_class import RobotControl

rc = RobotControl()
laser = rc.get_laser(360)

while laser > 1:
    rc.move_straight()
    laser = rc.get_laser(360)
    print("Current distance to wall: %f " % laser)

rc.stop_robot()
print("Wall is at %f meters" % laser)