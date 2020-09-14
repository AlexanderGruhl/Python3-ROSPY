from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(150)
print("Distance measured in laser1 is ", laser1)

laser2 = rc.get_laser(600)
print("Distance measured in laser2 is ", laser2)

laser2 = rc.get_laser(400)
print("New distance in laser2 is ", laser2)
