from robot_control_class import RobotControl

rc = RobotControl()

laser = rc.get_laser(360)

if(laser < 1):
    rc.stop_robot()
else:
    rc.move_straight()

print("Wall distance from robot is ", laser)